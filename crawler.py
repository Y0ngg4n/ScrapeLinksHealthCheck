from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse


class Crawler(CrawlSpider):
    def __init__(self, name, allowed_domains, start_urls):
        self.name = name
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        self.rules = (
            Rule(LinkExtractor(allow=('.*',)), callback='parse_item'),
        )
        self.links = set()
        super(Crawler, self).__init__()



    def parse_item(self, response):
        domain = urlparse(response.url).netloc
        f = open("links/"+domain+".txt", 'a')
        f.write(response.url + "\n")