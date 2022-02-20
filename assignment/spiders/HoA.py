import csv
import scrapy


class HoaSpider(scrapy.Spider):
    name = 'HoA'
    allowed_domains = ['www.hamropatro.com/']
    start_urls = ['http://www.hamropatro.com/']
    
    def __init__(self):
        self.all_urls=[]
        self.internal_link = 0
        self.external_link = 0
        
    def parse(self, response):
        f = open("urls.csv", "a")
        ## extraction of all the urls from the page
        for href in response.css('a::attr(href)').extract():
            ## relative links changed to absolute links
            if href.startswith('/') or not(href.startswith('http')):
                href = response.urljoin(href)
            ## writing the urls to the file urls.csv 
            ## cleaning some noise urls
            if href not in self.all_urls and "date" not in href and "calendar" not in href:     
                if "www.hamropatro.com" in href:
                    self.internal_link += 1
                else:
                    self.external_link += 1
                self.all_urls.append(href)
                writer = csv.writer(f)
                writer.writerow([href])
        f.close()
        ## Displaying the number of internal and external links
        print("Internal Link: ", self.internal_link)
        print("External Link: ", self.external_link)
        print("Total Link: ", len(self.all_urls))
        print("List of URLs can be found at urls.csv")
        if self.internal_link > self.external_link:
            print("The website is a authority")
        else:
            print("The website is a hub")
        
        
            
                
                
                
                    
        