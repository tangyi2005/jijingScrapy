# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import time

class JijingscrapyPipeline:
    def process_item(self, item, spider):
        return item

#保存到数据库
class mysqlPipeline:
    conn = None     # 连接
    cursor = None    # 游标,使用该连接创建并返回游标
    def open_spider(self, spider):
                        # Connect()参数说明
        # jdbc:mysql://localhost:3306/jijingMysql?useUnicode=true&characterEncoding=utf-8&useSSL=true&serverTimezone=UTC
        self.conn = pymysql.Connect(
            host='127.0.0.1',
            port= 3306,
            user= 'root',
            password= '12345678',
            db= 'jijingMysql',
            charset='utf8',
            use_unicode=True
        )

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:          # execute(op)     执行一个数据库的查询命令
            self.cursor.execute('insert into jijing_data ('
                                'ji_jing_id,'
                                'ji_fing_href,'
                                'ji_jing_title,'
                                'ji_jing_time,'
                                'net_value_unit,'
                                'cumulative_value,'
                                'day_growth,'
                                'nearly_week,'
                                'nearly_month,'
                                'early_three_months,'
                                'nearly_six_month,'
                                'nearly_one_year,'
                                'nearly_two_years,'
                                'early_three_years,'
                                'recent_years,'
                                'set_up_to) values'
                                '(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                ,(
                                    item['jiJingId'],
                                    item['jiJingHref'],
                                    item['jiJingTitle'],
                                    item['jiJingTime'],
                                    item['netValueUnit'],
                                    item['cumulativeValue'],
                                    item['dayGrowth'],
                                    item['nearlyWeek'],
                                    item['nearlyMonth'],
                                    item['earlyThreeMonths'],
                                    item['nearlySixMonth'],
                                    item['nearlyOneYear'],
                                    item['nearlyTwoYears'],
                                    item['earlyThreeYears'],
                                    item['recentYears'],
                                    item['setUpTo']))
            self.conn.commit()  # 提交当前事务
            print('成功了》》》')
        except Exception as e:
            print('问题数据跳过！......',e)
            time.sleep(2)
            self.conn.rollback()        # 回滚当前事务
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()