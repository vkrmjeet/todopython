'''
    this spider will scrap quotes form the website.
            #scrappy comes its own mechanism of scrapping data from a website , those are known as selectors.
            a selector can be css , xpath
    running spider and saving scrapped data
       scrapy runspider quotes.py-o quotes.xml
       you can also save in json or xml

'''

import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ['https://bluelimelearning.github.io/my-fav-quotes/https://bluelimelearning.github.io/my-fav-quotes/']

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote': quote.css('p.aquote::text').extract(),
                'author': quote.css('p.author::text').extract_first(),
            }