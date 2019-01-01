import scrapy
import re #正则匹配
from ZLZP.items import ZlzpItem

#爬取数据，再在pipelines里处理数据
class ZlzpSpider(scrapy.Spider):
    name = 'zlzp'
    #allowed_domains = ['http://news.bnu.edu.cn']#不注释的话 会爬不了
    page=1#从第一页开始爬
    front_urls='https://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=%E5%8C%97%E4%BA%AC&p='
    page_urls=front_urls+str(page)
    start_urls = [page_urls]#最初始的url
    def parse(self,response):
        #爬取各个类型的招聘信息的链接
        i=-1
        for type in response.xpath("//*[@id='search_jobtype_tag']/a"):
            i+=1
            if i==0:
                continue#跳过第一个“不限”
            type_url="https://sou.zhaopin.com/"+type.xpath("@href").extract_first()
            print("*****************",type_url)
            yield  scrapy.Request(type_url,callback=self.parse_each_page)
    def parse_each_page(self, response):
        #pass
        #爬取每一种类别下的每一页招聘信息
        i=-1#用来排除表头
        for work in response.xpath("//*[@id='newlist_list_content_table']/table"):#获取除表头外的所有招聘链接
            i += 1
            if i==0:
                continue#跳过表头
            url=work.xpath('tr[1]/td[1]/div/a[1]/@href').extract_first()#获取岗位链接
            print("################",url)
            yield scrapy.Request(url,callback=self.parse_dir_details)
            #使用scrapy.Request用以返回爬取的某条招聘信息的链接，再用callback函数对返回链接进行再次爬取从而获取招聘信息具体内容，将爬取数据处理给item
        #取下一页的
        next_page=response.xpath("//*[@class='pagesDown-pos']/a/@href").extract_first()
        yield  scrapy.Request(next_page,callback=self.parse_each_page)

    def parse_dir_details(self,response):#用来爬取某个招聘链接里的具体内容
        item=ZlzpItem()
        item['jobName'] =response.xpath("//div[@class='top-fixed-box']/div[1]/div[1]/h1/text()") .extract_first() # 岗位名称
        item['companyName'] =response.xpath("//div[@class='top-fixed-box']/div[1]/div[1]/h2/a/text()").extract_first()   # 公司名称
        item['companyProp']=response.xpath("//div[@class='company-box']/ul/li[2]/strong/text()").extract_first().replace(u'\xa0',u' ') #公司类型
        # 五险一金\带薪休假\员工旅游\周末双休\弹性工作\餐补\交通补助\年底双薪\股票期权
        #提取公司福利
        all_fuli=response.xpath("/html/body/div[5]/div[1]/div[1]/div[1]/span/text()").extract()
        #因为每个岗位可能有多个福利，就讲匹配到的内容用extract（）,就会返回一个列表，里面是提取到的所有福利的text
        #用一个7位的数组表示是否有这七个福利，有则将对应位置为1
        item['fuli']=[int(a_fuli in all_fuli) for a_fuli in ("五险一金\带薪休假\员工旅游\周末双休\弹性工作\餐补\交通补助\年底双薪\股票期权".split("\\"))]
        job_detail_path=response.xpath("//div[@class='terminalpage-left']/ul")
        item['salary'] =sum(float(i) for i in re.findall("\d+",job_detail_path.xpath("li[1]/strong/text()").extract_first().replace(u'\xa0',u' ')))/2   # 月薪
        item['workExperience'] =job_detail_path.xpath("li[5]/strong/text()").extract_first().replace(u'\xa0',u' ')   # 工作经验
        item['recruitmentNumber'] =job_detail_path.xpath("li[7]/strong/text()").extract_first().replace(u'\xa0',u' ')   # 招聘人数
        item['education'] =job_detail_path.xpath("li[6]/strong/text()").extract_first().replace(u'\xa0',u' ')   # 最低学历
        yield  item