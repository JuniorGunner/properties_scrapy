# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader.processors import MapCompose, TakeFirst
# from w3lib.html import remove_tags

class ScrapyCasamineiraItem(scrapy.Item):
    id = scrapy.Field()
    neighborhood = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    type = scrapy.Field()
    area_usable = scrapy.Field()
    n_bedroom = scrapy.Field()
    n_bathroom = scrapy.Field()
    n_suite = scrapy.Field()
    n_parking = scrapy.Field()
    price_sale = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
