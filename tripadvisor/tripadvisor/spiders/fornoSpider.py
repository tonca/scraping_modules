from __future__ import absolute_import

import scrapy
from tripadvisor.items import TripadvisorItem


class fornoSpider(scrapy.Spider):
   
    name = 'forno'
    # allowed_domains = ['example.com']

    def start_requests(self):
        urls = [
            'https://www.tripadvisor.it/Search?geo=187814&pid=3826&redirect=&startTime=1487929642870&uiOrigin=MASTHEAD&q=Pizzeria+forno+a+legna&returnTo=__2F__&searchSessionId=99C8C2018B318C217722D10C38644F791487874399192ssid'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        
        print 'parse!'
        for rest in response.css('div.info.poi-info'):

            name = rest.css('div.title > span::text').extract()[0]
            address = rest.css('div.address::text').extract()[0]
            ratings = rest.css('div.prw_rup.prw_common_location_rating_simple > span > img').xpath('@alt').extract()
            item = TripadvisorItem()
            match = rest.css('span.query-text').extract()
            
            item['name'] = name
            item['address'] = address
            item['ratings'] = ratings
            item['valid'] = len(match)>0

            yield item

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)