import scrapy


class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["producindetail.com", "www.productindetail.com"]
    start_urls = ["https://www.productindetail.com/phones"]

    def parse(self, response):
        products = response.css('div.card')

        for product in products:

            yield{
            'Product name' : product.css('strong::text').get(),
            'Brand' : product.css('strong::text').get().split()[0],
            'Image URL' : product.css('img ::attr(src)').get()
        }

       # next_page = response.css('[aria-label="Next"] ::attr(href)').get()

       # if next_page is not ('#'):
       #     next_page_url = 'https://www.productindetail.com' + next_page
       #     yield response.follow(next_page_url, callback=self.parse)
