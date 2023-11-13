# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import sys
from .items import PhonesItem

class ProductindetailPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:
    
    collection = 'phones'

    # The __init__() method gets those two variables from the crawler settings and stores them for later use. A check is made right away to see if a connection string is provided. If not, the application stops here.
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")


    # The from_crawler() function here enables you to inject parameters from the CLI into the __init__() function. Here, the function looks for the MONGODB_URI and MONGODB_DATABASE settings that will be passed using the -s argument with the scrapy crawl command.
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )


    # These functions use PyMongo to open a client that Scrapy will use throughout the whole lifecycle of the spider.
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # Start with a clean database
        self.db[self.collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()


    # Finally, the process_item() function processes every item passed to this pipeline. Here, items are saved to the database using insert_one() and then returned to be processed by the next pipeline, if any.
    def process_item(self, item, spider):
        data = dict(PhonesItem(item))
        self.db[self.collection].insert_one(data)
        return item