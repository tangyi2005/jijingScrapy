#encoding:utf-8
import json

import scrapy
import logging
from bs4 import BeautifulSoup
from ..model.tianTianItem import HonorItem
from ..extras import utils

class cnblogsData(scrapy.Spider):
    name = 'cnblogs'
    start_urls = ['http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn50;ddesc;qsd20200320;qed20210320;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb']
    model_urls = []
    # base_site = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s6yzf;pn50;ddesc;qsd20200320;qed20210320;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"

    def parse(self, response):
        driver = response.driver
        item = HonorItem()
        logging.debug("开始log对应")
        print('url:', response.url)
        print('new url:', response.urljoin('Zarten'))
        # data = json.loads(response.body)
        # print("这里有没经data:", data)
        res = BeautifulSoup(driver.page_source,'html.parser', from_encoding='utf-8')

        #基金数据
        # for link in res.find_all('tbody'):
        #     if link.find(type="checkbox"):
        #         # print("这里有没经01:", link)
        #         for link01 in link.find_all('tr'):
        #             jiJingId = link01.find_all('td')[0].input['id']
        #             print("这里有没经02:",jiJingId)
        #             item["jiJingId"] = jiJingId
        #             item["jiJingHref"] = link01.find_all('td')[2].a['href']
        #             item["jiJingTitle"] = link01.find_all('td')[3].a['title']
        #             item["jiJingTime"] = link01.find_all('td')[4].string
        #             item["netValueUnit"] = link01.find_all('td')[5].string
        #             item["cumulativeValue"] = link01.find_all('td')[5].string
        #             item["dayGrowth"] = link01.find_all('td')[7].string
        #             item["nearlyWeek"] = link01.find_all('td')[8].string
        #             item["nearlyMonth"] = link01.find_all('td')[9].string
        #             item["earlyThreeMonths"] = link01.find_all('td')[10].string
        #             item["nearlySixMonth"] = link01.find_all('td')[11].string
        #             item["nearlyOneYear"] = link01.find_all('td')[12].string
        #             item["nearlyTwoYears"] = link01.find_all('td')[13].string
        #             item["earlyThreeYears"] = link01.find_all('td')[14].string
        #             item["recentYears"] = link01.find_all('td')[15].string
        #             item["setUpTo"] = link01.find_all('td')[16].string
        #             yield item

        for link in res.find_all('tbody'):
            if link.find(type="checkbox"):
                # print("这里有没经01:", link)
                logging.debug("获取的页面数据 %s",link)
        a = res.find_all(id="pagebar")
        print("这里有多少数据瞒住条件", a)
        s = utils.find_element_by_css_selector(driver,"label[value='2']").click()
        cnblogsData.parse_details(driver)
        # yield scrapy.Request(response.url, callback=self.parse_detail)
        logging.debug("获取第二页请求的URL %s ", driver)
        # utils.find_element_by_css_selector(driver, "下一页").click()
        # yield scrapy.Request("https://www.baidu.com", callback=self.parse)
        # driver.find_element_by_link_text("下一页").click()
        # 退出，清除浏览器缓存
        driver.quit()



    def parse_model(self, response):
        res = BeautifulSoup(response.text)
        print("*****parse_model这里有没经", res)

    def parse_details(self,driver):
        print("*****parse_detail这里有没经")
        res = BeautifulSoup(driver.page_source, 'html.parser', from_encoding='utf-8')
        for link in res.find_all('tbody'):
            if link.find(type="checkbox"):
                # print("这里有没经01:", link)
                logging.debug("parse_detail获取的页面数据 %s",link)

    def closed(self, reason, response):  # 爬虫结束爬取后关闭浏览器对象
        print("*******closed")
        response.driver.quit()
