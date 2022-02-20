from matplotlib.font_manager import json_dump
import scrapy
import json

class AnnapurnaSpider(scrapy.Spider):
    name = 'annapurna'
    allowed_domains = ['annapurnapost.com']
    start_urls = ['https://bg.annapurnapost.com/api/news/list?page=1&per_page=20&category_alias=tech&isCategoryPage=1']
  

    def __init__(self):
        self.base_url = "https://bg.annapurnapost.com/api/news/list?page={}&per_page=20&category_alias=tech&isCategoryPage=1"
        self.counter = 1
        self.news_counter = 0
    
    def parse(self, response):
        data = json.loads(response.body)
        f = open("titles.txt", "a", encoding="utf-8")
        for news in data['data']:
            self.news_counter += 1
            title = news['title']
            f.write(title.strip())
        f.close()
        print("News Count: ", self.news_counter)
        if self.counter < 3:
            self.counter += 1
            url = self.base_url.format(self.counter)
            yield scrapy.Request(url=url, callback=self.parse)
        pass
