# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'LeParisien_news'
    start_urls = ['https://www.leparisien.fr/elections/presidentielle/']

    def parse(self, response):
        for quote in response.css('.story-headline'): # doens't work
            print ('header:', quote.css('::text').get())
            """
            yield {
                #'author': quote.xpath('span/small/text()').get(),
                #'text': quote.css('span.text::text').get(),
                'header': quote.css('::text').get()
            }
            """
"""
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
"""
