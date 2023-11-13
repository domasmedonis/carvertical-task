# carvertical-task

Scrapy requires Python 3.8+, either the CPython implementation (default) or the PyPy implementation (see Alternate Implementations).


Dependencies: 
Scrapy installation - pip install Scrapy
PyMongo installation - $ python3 -m pip install pymongo


Setting up a local MongoDB database : https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database
Setting up MongoDB Atlas : https://www.mongodb.com/docs/atlas/getting-started/


Run Scrapy (Saves the data into a json file saved in your machine) - scrapy crawl phones -O myData.json

Run Scrapy (Saves the data into a MongoDB database) - scrapy crawl -s MONGODB_URI="mongodb+srv://<YOUR_CONNECTION_STRING>" -s MONGODB_DATABASE="YourDatabase" phones
