# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 记录每一篇文章的信息
    title = scrapy.Field()
    read = scrapy.Field()
    like = scrapy.Field()
    review = scrapy.Field()
    collect = scrapy.Field()
