import scrapy


class WebFranceSpider(scrapy.Spider):
    name = "web-france"
    allowed_domains = ["www.sirene.fr"]
    start_urls = ["https://www.sirene.fr/"]

    def parse(self, response):
        pass
