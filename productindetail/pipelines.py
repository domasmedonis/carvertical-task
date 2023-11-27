# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


import pymongo

class MongoDBPipeline(object):

    def __init__(self) -> None:
        # Initialize the pipeline and connect to the MongoDB client
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.client['phone_data']['phones'] # Access the collection through the amazon database

    def close_spider(self, spider):
        # This will end DB connection when spider is interrupted or shutsdown
        self.client.close()

    def process_item(self, item, spider):
        # Insert the data to the collection and return message about the number of data added to the collection
        self.collection.insert_one(dict(item))
        return f"Total number of products scraped: {self.collection.count_documents({})}"
