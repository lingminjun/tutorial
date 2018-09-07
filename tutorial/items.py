# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    spuid = scrapy.Field()

    name = scrapy.Field()
    description = scrapy.Field()

    merchant = scrapy.Field()

    skuid0 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid1 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid2 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid3 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid4 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid5 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid6 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid7 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid8 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid9 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid10 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid11 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid12 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid13 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid14 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid15 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid16 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid17 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid18 = scrapy.Field()  # 嵌套 [ItemSKU]
    skuid19 = scrapy.Field()  # 嵌套 [ItemSKU]

    price = scrapy.Field()  # 售价
    orgprice = scrapy.Field()   # 原价 

    url = scrapy.Field()

    color = scrapy.Field()
    size = scrapy.Field()

    img0 = scrapy.Field()
    img1 = scrapy.Field()
    img2 = scrapy.Field()
    img3 = scrapy.Field()
    img4 = scrapy.Field()
    img5 = scrapy.Field()
    img6 = scrapy.Field()
    img7 = scrapy.Field()
    img8 = scrapy.Field()
    img9 = scrapy.Field()

    
    
