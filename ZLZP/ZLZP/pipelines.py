# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ZlzpPipeline(object):
    def __init__(self):
        self.f = open('result.csv','w',newline='')
        self.headers = ['jobName','companyName','companyProp','salary','workExperience','recruitmentNumber','education',
                   '五险一金','带薪休假','员工旅游','周末双休','弹性工作','餐补','交通补助','年底双薪','股票期权']
        self.writer = csv.writer(self.f)
        self.writer.writerow(self.headers)
    def process_item(self,item,spider):
        # f=open('result.csv','w',newline='')
        # headers=['jobName','companyName','companyType','salary','workExperience','recruitmentNumber','education','五险一金','带薪休假','员工旅游','周末双休','弹性工作','餐补','交通补助','年底双薪','股票期权']
        # writer=csv.writer(f)
        # writer.writerow(headers)
        arow=[]
        for i in self.headers[:7]:
            arow.append(item[i])
        for i in item['fuli']:
            arow.append(i)
        self.writer.writerow(arow)
        return item
    def close_spider(self, spider):
        self.f.close()
