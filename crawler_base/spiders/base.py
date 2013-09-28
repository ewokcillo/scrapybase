# coding=utf-8
import urlparse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from bs4 import BeautifulSoup
import datetime
import re

import crawler_base.items as items


class BaseSpider(CrawlSpider):
    name = 'base'
    #REQUIRED: allowed domains
    allowed_domains = ['example.net', ]

    #REQUIRED: start url
    start_urls = [
            'http://www.example.net/', ]

    #REQUIRED: rules to follow pagination and parser pages
    rules = [
        Rule(SgmlLinkExtractor(
            allow=['http://www.example.net/\?page=\d+'], unique=True), 'parse_item', follow=True),]

    def parse_item(self, response):
        html = BeautifulSoup(response.body)

        #REQUIRED: select item to save objects
        item = items.CrawlerBaseItem()
        item['url'] = response.url

        return item
