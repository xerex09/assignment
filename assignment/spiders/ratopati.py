from datetime import datetime
import scrapy


class RatopatiSpider(scrapy.Spider):
    name = 'ratopati'
    allowed_domains = ['ratopati.com']
    start_urls = ['https://ratopati.com/category/knowledge-science']
    
    def __init__(self):
        self.base_url = "https://ratopati.com/category/knowledge-science?page={}"
        self.counter = 1
        self.news_counter = 0

    def parse(self, response):
        
        titles = response.css('.ot-content-block a::text').extract()
        urls = response.css(".ot-content-block a::attr(href)").extract()
        last_url = urls[-2]
        last = last_url.split("/")
        new_date = last[3]+'-'+last[4]+'-'+last[5]
        self.date = datetime.strptime(new_date, "%Y-%m-%d").date()
        old_date = datetime.strptime("2021-08-01", "%Y-%m-%d").date()
        for i in urls:
            self.news_counter += 1
        print("News Count: ", self.news_counter)
        if self.date > old_date:
            self.counter +=1 
            yield scrapy.Request(url=self.base_url.format(self.counter), callback=self.parse)
        
        pass
