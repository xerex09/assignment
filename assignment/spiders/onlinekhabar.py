import scrapy


class OnlinekhabarSpider(scrapy.Spider):
    name = 'onlinekhabar'
    allowed_domains = ['www.onlinekhabar.com']
    start_urls = ['https://www.onlinekhabar.com/content/business/technology/']

    def parse(self, response):
        pass
