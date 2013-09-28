# Scrapy settings for crawler_base project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler_base'

SPIDER_MODULES = ['crawler_base.spiders']
NEWSPIDER_MODULE = 'crawler_base.spiders'


DOWNLOAD_DELAY = 0.5

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib_exp.downloadermiddleware.decompression.DecompressionMiddleware': None
}

#USER_AGENT = 'crawler_base (+http://www.yourdomain.com)'

#mongodb

ITEM_PIPELINES = [
          'scrapymongodb.MongoDBPipeline',
          ]

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items'
MONGODB_UNIQ_KEY = 'url'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True
