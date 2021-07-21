import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'LeParisien_news'
    start_urls = ['https://edition.cnn.com/world']

    def parse(self, response):
        #for quote in response.css('div#h2.story-headline'): # doens't work
        # for quote in response.css('h2.story-headline'): # doens't work
        # for quote in response.css('.main__feed__title'): NOK
        # for quote in response.css('.main__feed__title a'): NOK
        # for quote in response.css('.js-indicators , .main__big__title , .main__feed__title'): NOK
        # for quote in response.css('.js-indicators , .main__big__title , .main__feed__title a'): NOK
        # for quote in response.css('.js-main-reload-item span'):
        for quote in response.css('.cd--vertical .vid-left-enabled'):
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
