import scrapy
import json
import csv

class FornoSpider(scrapy.Spider):

    name = 'forno'

    def start_requests(self):
        urls = [
            'https://www.tripadvisor.it/Search?geo=187814&pid=3826&redirect=&startTime=1488192203037&uiOrigin=MASTHEAD&q=forno+a+legna&returnTo=https%253A__2F____2F__www__2E__tripadvisor__2E__it__2F__Restaurant__5F__Review__2D__g187814__2D__d1145265__2D__Reviews__2D__Pizzeria__5F__Alla__5F__Lampara__2D__Udine__5F__Province__5F__of__5F__Udine__5F__Friuli__5F__Venezia__5F__Giulia__2E__html&searchSessionId=99C8C2018B318C217722D10C38644F791488192199998ssid'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        
        print 'parse!'
        json_file = open('fornoalegna.json', 'wb')
        print "JSON open!"
        csv_file = open('fornoalegna.csv', 'wb')
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for rest in response.css('div.info.poi-info'):

            name = rest.css('div.title > span::text').extract()[0]
            address = rest.css('div.address::text').extract()[0]
            ratings = rest.css('div.prw_rup.prw_common_location_rating_simple > span > img').xpath('@alt').extract()
            match = rest.css('span.query-text').extract()
            
            item = {}
            item['name'] = name
            item['address'] = address
            item['ratings'] = ratings
            item['valid'] = len(match)>0

            spamwriter.writerow([address * 5 + ['Baked Beans'])

            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            

        self.file.close()
        print "JSON closed!"

 