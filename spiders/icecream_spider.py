import scrapy

class IceCreamSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'http://www.benjerry.com/flavors'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        flavor = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % flavor
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)