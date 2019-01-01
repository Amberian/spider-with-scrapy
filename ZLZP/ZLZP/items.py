# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #jobName,companyName,companyProp,companyScale,education,id,jobAddress,recruitmentNumber,workExperience,
    # 五险一金,带薪休假,员工旅游,周末双休,弹性工作,餐补,交通补助,年底双薪,股票期权,treatment_nums,salary
    jobName=scrapy.Field()#岗位名称
    companyName=scrapy.Field()#公司名称
    companyProp=scrapy.Field()#公司类型
    salary=scrapy.Field()#月薪
    workExperience=scrapy.Field()#工作经验
    recruitmentNumber=scrapy.Field()#招聘人数
    education=scrapy.Field()#最低学历
   #福利：五险一金\带薪休假\员工旅游\周末双休\弹性工作\餐补\交通补助\年底双薪\股票期权
    fuli=scrapy.Field()
    pass
