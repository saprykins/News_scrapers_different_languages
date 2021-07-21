import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'LeParisien_news'
    start_urls = ['https://www.tsa-algerie.com/economie/']

    def parse(self, response):
        #for quote in response.css('div#h2.story-headline'): # doens't work
        # for quote in response.css('h2.story-headline'): # doens't work
        for quote in response.css('.title-middle a'): # doens't work
            #print ('header:', quote.css('::text').get())

            yield {
                #'author': quote.xpath('span/small/text()').get(),
                #'text': quote.css('span.text::text').get(),
                'header': quote.css('a ::text').get()
            }

"""
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
"""
