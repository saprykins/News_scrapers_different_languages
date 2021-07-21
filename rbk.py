# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'rbk'
    start_urls = ['https://www.rbc.ru/']

    def parse(self, response):
        #for quote in response.css('div#h2.story-headline'): # doens't work
        # for quote in response.css('h2.story-headline'): # doens't work
        # for quote in response.css('.main__feed__title'): NOK
        # for quote in response.css('.main__feed__title a'): NOK
        # for quote in response.css('.js-indicators , .main__big__title , .main__feed__title'): NOK
        # for quote in response.css('.js-indicators , .main__big__title , .main__feed__title a'): NOK
        # for quote in response.css('.js-main-reload-item span'):
        #for quote in response.css('.js-main-reload-item span'):
        for quote in response.css('.main__feed__title'): # works in terminal, shows 10 elements w/o trash
            #print ('header:', quote.css('::text').get())# works in terminal, shows 10 elements w/o trash
            yield {
                #'author': quote.xpath('span/small/text()').get(),
                #'text': quote.css('span.text::text').get(),
                'header': quote.css('::text').get()
            }
"""
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
"""
