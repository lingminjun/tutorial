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

    price = scrapy.Field()  # 售价
    orgprice = scrapy.Field()   # 原价 

    url = scrapy.Field()

    color = scrapy.Field()
    size = scrapy.Field()

    img0 = scrapy.Field()

    colorskuid0 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid1 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid2 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid3 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid4 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid5 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid6 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid7 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid8 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid9 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid10 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid11 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid12 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid13 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid14 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid15 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid16 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid17 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid18 = scrapy.Field()  # 嵌套 [ItemSKU]
    colorskuid19 = scrapy.Field()  # 嵌套 [ItemSKU]
    
    colorimg0 = scrapy.Field()
    colorimg1 = scrapy.Field()
    colorimg2 = scrapy.Field()
    colorimg3 = scrapy.Field()
    colorimg4 = scrapy.Field()
    colorimg5 = scrapy.Field()
    colorimg6 = scrapy.Field()
    colorimg7 = scrapy.Field()
    colorimg8 = scrapy.Field()
    colorimg9 = scrapy.Field()

    
    
