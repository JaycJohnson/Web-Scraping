import scrapy

class WikipediaSpider(scrapy.spider):
    name = "Wikipedia"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Biological_engineering'
        ]
        for url in urls:
            yield srapy.Request(url=url, callback=self.parse)
            
def parse(self, response):
    print(response)

