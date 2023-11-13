# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhonesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    operating_system = scrapy.Field()
    display_technology = scrapy.Field()
    image_url = scrapy.Field()