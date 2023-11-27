import scrapy
from ..items import PhonesItem


class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["producindetail.com", "www.productindetail.com"]
    start_urls = ["https://www.productindetail.com/phones"]

    def parse(self, response):

        # Goes to phone's details page
        urls = response.css('div.card-body > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


       #Pagination
     #   next_page = response.css('[aria-label="Next"] ::attr(href)').get()
      #  if next_page is not ('#'):
       #     next_page_url = 'https://www.productindetail.com' + next_page
       #     yield response.follow(next_page_url, callback=self.parse)


        # Data 
    def parse_details(self, response):
            item = PhonesItem()            

            item['name'] = response.css('h1.fs-2 > strong::text').extract_first(),
            item['brand'] = response.css('h1.fs-2 >strong::text').extract_first().split()[0],
            item['description'] = response.css('p.mb-0::text').extract_first(), # not sure if it's the right description
            item['operating_system'] = response.css('div.div > small::text').extract()[3],
            item['display_technology'] = response.css('[id="display"] td.border-end > small::text').extract()[1],
            item['image_url'] = response.css('div.row.mb-4 img.mb-3::attr(src)').extract_first()

            yield item
