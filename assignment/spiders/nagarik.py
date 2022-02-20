from datetime import datetime
import scrapy


class NagarikSpider(scrapy.Spider):
    name = 'nagarik'
    allowed_domains = ['nagariknews.nagariknetwork.com']
    start_urls = ['https://nagariknews.nagariknetwork.com/technology/']

    def __init__(self):
        self.date = 0
        self.news_counter = 0
        self.counter = 0
          
    def parse(self, response):
        title = response.css("article h1 a::text").extract()
        self.date = response.css("time").attrib["data-pdate"]
        self.date = datetime.strptime(self.date, "%Y-%m-%d %H:%M:%S").date()
        f = open("titles.txt", "a", encoding="utf-8")
        for i in title:
            self.news_counter += 1
            f.write(i.strip())         
        f.close()
        old_date = datetime.strptime("2021-08-01", "%Y-%m-%d").date()
        print("News Count: ", self.news_counter)
        print("Date: ", self.date)
        print("Old Date: ", old_date)
        if self.date > old_date:
            self.counter += 1
            url = self.start_urls[0]+"?offset="+str(self.counter*24)+"&ajax=true"
            yield scrapy.Request(url=url, callback=self.parse)
        pass
