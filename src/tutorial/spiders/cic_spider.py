from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy import Item
from scrapy import Field

import os




class UrlItem(Item):
    url = Field()


class CicSpider(CrawlSpider):
    name = 'cic'
    allowed_domains = ['cic.unb.br']
    start_urls = ['http://cic.unb.br/professores-aposentados/']
    

    rules = (
        Rule(LinkExtractor(allow=r'professores-aposentados/.*'), callback='parse_url'),
    )
    
    # put all links in a general csv file and each body in a specific html file called pt_BR inside a folder with the same name as the link
    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url
        yield item
        # create a folder with the same name as the link
        folder = response.url.split('/')[-1]
        if not os.path.exists(folder):
            os.makedirs(folder)
        # create a html file with the body of the link
        with open(folder + '/pt_BR.html', 'wb') as f:
            f.write(response.body)