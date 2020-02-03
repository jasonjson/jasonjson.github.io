---
layout: post
title: Build crawler using scrapy
date: 2017-02-26 21:41
tags:
- Python
categories:
- Reading Notes
author: Jason
---
**Build crawler using scrapy**

## Build the project
`$scrapy startproject my_crawler`
该命令会在当前目录下创建一个名为”my_crawler”的工程，工程的目录结构如下

## Modify fields that you want
 修改”items.py”文件，在”MyCrawlerItem”类中加上如下代码：

```python
import scrapy
class MyCrawlerItem(scrapy.Item):
    title = scrapy.Field()    # 文章标题
    url = scrapy.Field()      # 文章地址
    summary = scrapy.Field()  # 文章摘要
    pass
```

## Add websites and html fields
在”my_crawler/spiders”目录下，创建一个名为”crawl_spider.py”文件（文件名可以任意取）。代码如下

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from my_crawler.items import MyCrawlerItem
class MyCrawlSpider(CrawlSpider):
    name = 'my_crawler'               # Spider名，必须唯一，执行爬虫命令时使用
    allowed_domains = ['mickeyliu5.github.io']   # 限定允许爬的域名，可设置多个
    start_urls = [
        "https://mickeyliu5.github.io/blog",   # 种子URL，可设置多个
    ]
    rules = ( # 对应特定URL，设置解析函数，可设置多个
        Rule(LinkExtractor(allow=r'/page[0-9]*'),  # 指定允许继续爬取的URL格式
                           callback='parse_item',   # 用于解析网页的回调函数名
                           follow=True
        ),
    )
    def parse_item(self, response):
        # 通过XPath获取Dom元素
    articles = response.xpath('//ul[@class="post-list"]/*')

    for article in articles:
        item = MyCrawlerItem()
        try:
            item['title'] = article.xpath('h2/a/text()').extract()[0]
            item['url'] = "mickeyliu5.github.io/{0}".format(article.xpath('h2/a/@href').extract()[0])
            item['summary'] = article.xpath('div[@class="post-excerpt"]/p/strong/em/text()').extract()[0]
            yield item
        except:
            pass
```
对于XPath不熟悉的朋友，可以通过Chrome的debug工具获取元素的XPath, view->developer->developer tools
[Some tutorials for XPath](https://www.w3schools.com/xml/xpath_syntax.asp)
## Test the crawler
`scrapy crawl my_crawler`
注意，这里的”my_crawler”就是你在”crawl_spider.py”文件中起的Spider名。

## Store the results into a json file
`scrapy crawl my_crawler -o my_crawler.json -t json`

## Store the results to mongodb
这里我们采用MongoDB，你需要先安装Python的MongoDB库”pymongo”。编辑”my_crawler”目录下的”pipelines.py”文件，在”MyCrawlerPipeline”类中加上如下代码：

```python
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
class MyCrawlerPipeline(object):
    def __init__(self):
        # 设置MongoDB连接
        client = MongoClient("mongodb://{0}:{1}".format().
            settings['MONGO_SERVER'],
            settings['MONGO_PORT']
        )
        db = client[settings['MONGO_DB']]
        self.collection = db[settings['MONGO_COLLECTION']]
    # 处理每个被抓取的MyCrawlerItem项
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:  # 过滤掉存在空字段的项
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # 也可以用self.collection.insert(dict(item))，使用upsert可以防止重复项
            self.collection.update({'url': item['url']}, dict(item), upsert=True)
        return item
```
再打开”my_crawler”目录下的”settings.py”文件，在文件末尾加上pipeline的设置：

```python
ITEM_PIPELINES = {
    'my_crawler.pipelines.MyCrawlerPipeline': 300,    # 设置Pipeline，可以多个，值为执行优先级
}
# MongoDB连接信息
MONGO_SERVER = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'scrapy'
MONGO_COLLECTION = 'posts'
DOWNLOAD_DELAY=2    # 如果网络慢，可以适当加些延迟，单位是秒
```

别忘了启动MongoDB并创建”bjhee”数据库哦。现在你可以在MongoDB里查询到记录了。

## In summary
What you need to do to build a crawler
1. “items.py”中定义爬取字段
2. 在”spiders”目录下创建你的爬虫，编写解析函数和规则
3. “pipelines.py”中对爬取后的结果做处理
4. “settings.py”设置必要的参数

[Some blogs about scrapy](http://www.cnblogs.com/twelfthing/articles/4620533.htmli)
