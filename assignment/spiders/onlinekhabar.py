import scrapy
from datetime import datetime


class OnlinekhabarSpider(scrapy.Spider):
    name = 'onlinekhabar'
    allowed_domains = ['www.onlinekhabar.com']
    start_urls = ['https://www.onlinekhabar.com/content/business/technology/']
    
    def __init__(self):
        self.date = 0
        self.base_url = "https://www.onlinekhabar.com/content/business/technology/page/{}"
        self.counter = 1
        self.news_counter = 0
        
    def parse(self, response):
        titles = response.css('.ok-grid-12 .ok-news-title-txt::text').extract()
        urls = response.css(".ok-grid-12 .ok-news-post a::attr(href)").extract()
        last_url = urls[-1]
        last  = last_url.split("/")
        new_date = last[3]+'-'+last[4]+'-'+'1'
        self.date = datetime.strptime(new_date, "%Y-%m-%d").date()
        old_date = datetime.strptime("2021-08-01", "%Y-%m-%d").date()
        f = open("titles.txt", "a", encoding="utf-8")
        for title in titles:
            self.news_counter += 1
            f.write(title.strip())
        f.close()
        print("News Count: ", self.news_counter)
        if self.date > old_date:
            self.counter +=1 
            yield scrapy.Request(url=self.base_url.format(self.counter), callback=self.parse)
        pass
