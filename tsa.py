import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'tsa_news'
    start_urls = [
        'https://www.tsa-algerie.com/economie/',
        'https://www.tsa-algerie.com/politique/',
        'https://www.tsa-algerie.com/societe/'
    ]

    def parse(self, response):
        for quote in response.css('.title-middle a'):
            yield {
                'header': quote.css('::text').get(),
                #'link': quote.css('::text').get()
                'link': quote.css('a').attrib['href']
                #'header': quote.css('a ::text').get() works well
                #'header': quote.css('a ::href').get() doesn't work
                #'link': quote.css('a href').get() empty list
            }
"""
doesn't work though due to a wrong selector
quote = response.css("h1.article-preview__title title-middle transition")[0]
text = quote.css("a::text").get()
link = quote.css("a").attrib['href'].get()
"""

"""
let's keep it
quote = response.css('.title-middle a')[0] # works
text = quote.css("::text").get() # works
link = quote.css('a').attrib['href'] # works
"""
