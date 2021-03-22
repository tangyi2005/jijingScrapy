import scrapy

class HonorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 基金ID
    jiJingId = scrapy.Field()
    # 基金详解url
    jiJingHref = scrapy.Field()
    #名称
    jiJingTitle = scrapy.Field()
    #数据时间
    jiJingTime = scrapy.Field()
    #单位净值
    netValueUnit = scrapy.Field()
    #累计净值
    cumulativeValue = scrapy.Field()
    #日增长率
    dayGrowth = scrapy.Field()
    #近1周
    nearlyWeek = scrapy.Field()
    #近1月
    nearlyMonth = scrapy.Field()
    #近3月
    earlyThreeMonths = scrapy.Field()
    #近6月
    nearlySixMonth = scrapy.Field()
    #近1年
    nearlyOneYear = scrapy.Field()
    #近2年
    nearlyTwoYears = scrapy.Field()
    #近3年
    earlyThreeYears = scrapy.Field()
    #今年来
    recentYears = scrapy.Field()
    #成立来
    setUpTo = scrapy.Field()
    # 创建时间
    creationTime = scrapy.Field()
    # 更新时间
    updateTime = scrapy.Field()
    # 创建的日期
    creationDate = scrapy.Field()
