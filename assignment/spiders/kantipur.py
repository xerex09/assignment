from datetime import datetime
import re
from matplotlib.pyplot import title
import scrapy


class KantipurSpider(scrapy.Spider):
    name = 'kantipur'
    allowed_domains = ['ekantipur.com']
    start_urls = ['https://ekantipur.com/technology/2022/02/18/']
    
    def __init__(self):
        self.date = 0
        self.url_counter = 0
        self.base_url = "https://ekantipur.com/technology/" 
        
    def parse(self, response):
        titles = response.css("article h2 a::text").extract()
        urls = response.css("article h2 a::attr(href)").extract()
        last_url = urls[-1]
        last = last_url.split("/")
        new_date = last[2]+'-'+last[3]+'-'+last[4]
        self.date = datetime.strptime(new_date, "%Y-%m-%d").date()
        new_url = self.base_url+new_date.replace("-","/")+"/"
        old_date = datetime.strptime("2021-08-01", "%Y-%m-%d").date()
        f = open("titles.txt", "a", encoding="utf-8")
        for title in titles:
            self.url_counter += 1
            f.write(title.strip())
        f.close()
        print("News Count: ", self.url_counter)
        if self.date > old_date:
            yield scrapy.Request(url=new_url, callback=self.parse)
        pass