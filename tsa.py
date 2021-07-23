import scrapy
"""
selectors for main-tsa-page

time
response.css("time.ntdga__date::attr(datetime)")[0].get()
response.css("article time.ntdga__date::attr(datetime)")[0].get()

title
response.css(".ntdga__title a::text")[0].get()
response.css("article.ntdga a::text")[0].get()

subject
response.css(".ntdga__date a::text")[0].get()
response.css("article .ntdga__date a::text")[0].get()
"""

class QuotesSpider(scrapy.Spider):
    name = 'tsa_news'
    start_urls = [
        'https://www.tsa-algerie.com/'
        #'https://www.tsa-algerie.com/politique/'
    ]

    def parse(self, response):
        # selector".title-middle a" has much trash in addition to titles,
        # and works better than ".transition a"

        # for quote in response.css('.title-middle a'): # doesn't work with main-tsa-page
        for quote in response.css('article'): # shows only 3

        # for quote in response.css('.article a'): # shows nothing
        # for quote in response.css('article.article-preview'): # shows nothing
        # for quote in response.css('.transition a'):# shows nothing
            yield {
                #'header': quote.css('::text').get(), it worked
                #'link': quote.css('a ::attr(href)').get() #it worked

                # getting publish time
                #'date':
                #'link': quote.css('::text').get()
                #'header': quote.css('a ::text').get() works well
                #'header': quote.css('a ::href').get() doesn't work
                #'link': quote.css('a href').get() empty list

                # title
                #'title': response.css(".ntdga a::text")[0].get(), # selector found on page, shows the same info #-times
                'title': quote.css(".ntdga__title a::text")[0].get(),

                # time
                'time': quote.css("time.ntdga__date::attr(datetime)").get(),

                # subject
                'subject': quote.css(".ntdga__date a::text")[0].get()
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
