import scrapy


class IceCreamSpider(scrapy.Spider):
    name = "icecream"

    def start_requests(self):
        urls = [
            'http://www.benjerry.com/flavors'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        flavors = response.css('description').xpath('//h4/text()').extract()
        filename = 'flavors.html'
        with open(filename, 'wb') as f:
            for flavor in flavors:
                f.write(flavor)
                f.write('\n')
        self.log('Saved file %s' % filename)
