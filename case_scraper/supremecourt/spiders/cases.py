import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class Case(scrapy.Item):
    link = scrapy.Field()
    pdf_link = scrapy.Field()
    judgment_link = scrapy.Field()

class CrawlSpider(CrawlSpider):
    name = 'sccases'
    base_link = 'www.supremecourt.uk'
    allowed_domains = [base_link]
    start_urls = ['https://www.supremecourt.uk/decided-cases/index.html']
    case_links = LinkExtractor(allow=r'/cases/')
    all_link = LinkExtractor(allow=r'/decided-cases/')
    rules = [
        Rule(case_links,
        callback='parse_case',
        follow = False),
        Rule(all_link,
             follow=True)
        ]
    def parse_case(self, response):
        item = Case()
        item["link"] = response
        item["judgment_link"] = response.xpath("//a[@title='Judgment (PDF)']/@href").extract_first()
        item["pdf_link"] = response.xpath("//a[@title='Press summary (PDF)']/@href").extract_first()
        if not item["pdf_link"]:
            item["pdf_link"] = response.xpath("//a[@title='Press Summary']/@href").extract_first()
        if not item["pdf_link"]:   
            item["pdf_link"] = response.xpath("//a[@title='Press summary HTML version']/@href").extract_first()
        if not item["pdf_link"]:   
            item["pdf_link"] = response.xpath("//a[@title='Press Summary HTML version']/@href").extract_first()


        return item
