import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'tsa_news'
    start_urls = ['https://www.tsa-algerie.com/economie/']

    def parse(self, response):
        for quote in response.css('.title-middle a'):
            yield {
                'header': quote.css('a ::text').get()
            }
