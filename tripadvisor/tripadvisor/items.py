# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from __future__ import absolute_import


import scrapy

class TripadvisorItem(scrapy.Item):

    # define the fields for your item here like:
    name = scrapy.Field()
    address = scrapy.Field()
    ratings = scrapy.Field()
    review_num = scrapy.Field()
    valid = scrapy.Field()