import scrapy

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"

    base_url = 'https://en.wikipedia.org'
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Biological_engineering'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        filename = response.url.split('/')[4]+'.txt' 
        with open(filename, 'w+') as f:
            for h3 in response.xpath('//p//a/@href').getall():
                f.write(h3 +'\n')
                url = self.base_url + h3
                yield scrapy.Request(url, self.parse_next_page)
        print(response)

    def parse_next_page(self, response):
        filename = response.url.split('/')[4]+'.txt' 
        with open(filename, 'w+') as f:
            for h3 in response.xpath('//p//a/@href').getall():
                f.write(h3 +'\n')
