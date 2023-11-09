import scrapy


class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["producindetail.com", "www.productindetail.com"]
    start_urls = ["https://www.productindetail.com/phones"]

    def parse(self, response):

        urls = response.css('div.card-body > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
       
       
       # next_page = response.css('[aria-label="Next"] ::attr(href)').get()

       # if next_page is not ('#'):
       #     next_page_url = 'https://www.productindetail.com' + next_page
       #     yield response.follow(next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
            'Product name' : response.css('div > h1 > strong::text').extract_first(),
            'Brand' : response.css('div > h1 >strong::text').extract_first().split()[0],
            'Operating system' : response.css('div > small ::text').extract()[3],
            'Display technology' : response.css('[id="display"] > div > table > tbody > tr > td > small::text').extract()[1],
            'Image URL' : response.css('div.card > div > div > div > img::attr(src)').extract_first()
        }