
from scrapy import Request, Spider
from urllib.parse import quote
from tutorial.items import *


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["list.tmall.com"]

    # start_urls = [
    #     "https://list.tmall.com/search_product.htm?q=%C1%AC%D2%C2%C8%B9&sort=s&style=g&type=pc&s=0",
    # ]

    '''
    scrapy spider参数使用该-a选项在爬网命令中传递。例如：
        scrapy crawl myspider -a category=electronics -a domain=system
    
    scrapy spider可以在其初始化程序中访问参数：
        class MySpider(scrapy.Spider):
            name = 'myspider'

            def __init__(self, category='', **kwargs):
                self.start_urls = ['http://www.example.com/category/%s' % category]
                super().__init__(**kwargs)  # python3
                self.log(self.domain)  # system
    '''
    def __init__(self, **kwargs):
        #  加载 chrome driver, 它的下载地址位于 https://sites.google.com/a/chromium.org/chromedriver/
        super().__init__(**kwargs)
        # 代码迁移到middlewares中
        # self.driver = webdriver.Chrome('/Users/lingminjun/chromedriver/chromedriver')
        # self.wait = WebDriverWait(self.driver, 10)

   
    #  针对规则的url开始爬取
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            print(keyword)
            for page in range(0, self.settings.get('MAX_PAGE')):
                offset = page * 60
                url = "https://list.tmall.com/search_product.htm?q=" + quote(keyword) + "&sort=s&style=g&type=pc&s=" + str(offset)
                print(url)
                yield Request(url=url, callback=self.parse)

    '''
    # 其他列表
    start_urls = [
        "https://list.tmall.com/search_product.htm?q=%C1%AC%D2%C2%C8%B9&sort=s&style=g&type=pc&s=0",
        "https://list.tmall.com/search_product.htm?q=%B0%EB%C9%ED%C8%B9&sort=s&style=g&type=pc&s=0"
        "https://list.tmall.com/search_product.htm?q=%B0%EB%C9%ED%C8%B9&sort=s&style=g&type=pc&s=60"
        "https://list.tmall.com/search_product.htm?q=%B0%EB%C9%ED%C8%B9&sort=s&style=g&type=pc&s=120"
    ]
    '''

    # #  模拟浏览器页面滚到页面底部的行为
    # def scroll_until_loaded(self):
    #     check_height = self.driver.execute_script("return document.body.scrollHeight;")
    #     while True:
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         try:
    #             self.wait.until(
    #                 lambda driver: self.driver.execute_script("return document.body.scrollHeight;") > check_height)
    #             check_height = self.driver.execute_script("return document.body.scrollHeight;")
    #         except TimeoutException:
    #             break

    def parse(self, response):

        print("开始解析数据。。。。。。。。。。。。。。。。。。。。。。")

        # 直接在这里等待浏览器滚动到底部实现-----也可以放到middlewares中来实现
        # self.driver.get(response.url)
        # 打开页面后，滑动至页面底部
        # self.scroll_until_loaded()

        '''
        <div class="product  " data-id="568226584526" data-atp="a!,,50010850,,,,,,,,">
            <div class="product-iWrap">
                <div class="productImg-wrap">
                    <a href="https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.44cd27f3kTXh3d&amp;id=568226584526&amp;areaId=310100&amp;user_id=520408396&amp;cat_id=50025135&amp;is_b=1&amp;rn=59ba062a25746b358c57d4b6d4dd8633&amp;sku_properties=1627207:7737315" class="productImg" target="_blank" data-p="2-10" data-spm-anchor-id="a220m.1000858.1000725.6" atpanel="2-10,568226584526,50010850,,spu,1,spu,520408396,,,">
                        <img src="https://img.alicdn.com/bao/uploaded/TB1Wap.rKGSBuNjSspbL6UiipXa_b.jpg" data-spm-anchor-id="a220m.1000858.1000725.i13.44cd27f3kTXh3d">
                    </a>

                </div>

                <div class="productThumb clearfix">
                    <div class="proThumb-wrap" data-spm-anchor-id="a220m.1000858.1000725.i7.44cd27f3kTXh3d">
                        <p class="ks-switchable-content">
                            <b data-sku="1627207:6847508" class="proThumb-img" data-index="2:1">
                                <img atpanel="2-1,568226584526,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB11y0jf7omBKNjSZFqL6RtqVXa_30x30.jpg" data-spm-anchor-id="a220m.1000858.1000725.i2.44cd27f3kTXh3d">
                                <i></i>
                            </b>
                            <b data-sku="1627207:7311498" class="proThumb-img" data-index="2:2">
                                <img atpanel="2-2,568226584526,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1L4x5fyMnBKNjSZFCL6R0KFXa_30x30.jpg" data-spm-anchor-id="a220m.1000858.1000725.i3.44cd27f3kTXh3d">
                                <i></i>
                            </b>
                            <b data-sku="1627207:7737315" class="proThumb-img proThumb-selected" data-index="2:3">
                                <img atpanel="2-3,568226584526,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1Wap.rKGSBuNjSspbL6UiipXa_30x30.jpg" data-spm-anchor-id="a220m.1000858.1000725.i4.44cd27f3kTXh3d">
                                <i></i>
                            </b>
                        </p>
                    </div>
                </div>

                <p class="productPrice" data-spm-anchor-id="a220m.1000858.1000725.i10.44cd27f3kTXh3d">
                    <a class="tag" atpanel=",568226584526,50010850,,spu,1,spu,,,,"><img src="//img.alicdn.com/tfs/TB1vKXIvHZnBKNjSZFhXXc.oXXa-30-30.png" title=""></a>

                    <em title="139.00"><b>¥</b>139.00</em>

                </p>

                <p class="productTitle">

                    <a href="//detail.tmall.com/item.htm?spm=a220m.1000858.1000725.7.44cd27f3kTXh3d&amp;id=568226584526&amp;skuId=3799403118816&amp;areaId=310100&amp;user_id=520408396&amp;cat_id=50025135&amp;is_b=1&amp;rn=59ba062a25746b358c57d4b6d4dd8633" target="_blank" title="一字肩连衣裙女夏装2018新款棉立方纯棉流苏蕾丝高腰气质复古裙子" data-p="2-11" data-spm-anchor-id="a220m.1000858.1000725.7" atpanel="2-11,568226584526,50010850,,spu,1,spu,520408396,,,">
                        棉立方一字肩纯棉流苏蕾丝高腰复古裙
                    </a>

                </p>

                <div class="productShop" data-atp="b!2-3,{user_id},,,,,,">
                    <a class="productShop-name" href="//store.taobao.com/search.htm?spm=a220m.1000858.1000725.8.44cd27f3kTXh3d&amp;user_number_id=520408396&amp;rn=59ba062a25746b358c57d4b6d4dd8633&amp;keyword=连衣裙" target="_blank" data-spm-anchor-id="a220m.1000858.1000725.8" atpanel="2-3,,,,spu,2,spu,">
                        棉立方旗舰店
                    </a>
                </div>
                <p class="productStatus">
                    <span>月成交 <em>823笔</em></span>
                    <span>评价 <a href="//detail.tmall.com/item.htm?spm=a220m.1000858.1000725.9.44cd27f3kTXh3d&amp;id=568226584526&amp;skuId=3799403118816&amp;areaId=310100&amp;user_id=520408396&amp;cat_id=50025135&amp;is_b=1&amp;rn=59ba062a25746b358c57d4b6d4dd8633&amp;on_comment=1#J_TabBar" target="_blank" data-p="2-1" data-spm-anchor-id="a220m.1000858.1000725.9" atpanel="2-1,568226584526,50010850,,spu,1,spu,520408396,,,">5187</a></span>
                    <span data-icon="small" class="ww-light ww-small" data-item="568226584526" data-nick="棉立方旗舰店" data-tnick="棉立方旗舰店" data-display="inline" data-atp="a!2-2,,,,,,,520408396"><a href="https://amos.alicdn.com/getcid.aw?spm=a220m.1000858.1000725.10.44cd27f3kTXh3d&amp;v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E6%A3%89%E7%AB%8B%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobaolmj_test" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。" data-spm-anchor-id="a220m.1000858.1000725.10"><span>旺旺在线</span></a></span>
                </p>
            </div>

        </div>
        '''
        for sel in response.xpath('//div[@class="product  "]'):
            item = TutorialItem()
            item['spuid'] = self.getxpathvalue(sel.xpath('./@data-id').extract())
            
            item['url'] = self.getxpathlink(sel.xpath('div[@class="product-iWrap"]/div[@class="productImg-wrap"]/a/@href').extract())
            
            item['img0'] = self.getxpathlink(sel.xpath('div[@class="product-iWrap"]/div[@class="productImg-wrap"]/a/img/@src').extract())
            
            item['price'] = self.getxpathvalue(sel.xpath('div[@class="product-iWrap"]/p[@class="productPrice"]/em/@title').extract())
            item['name'] = self.getxpathvalue(sel.xpath('div[@class="product-iWrap"]/p[@class="productTitle"]/a/text()').extract())
            
            item['merchant'] = self.getxpathvalue(sel.xpath('div[@class="product-iWrap"]/div[@class="productShop"]/a/text()').extract())

            idx = 0
            for b in sel.xpath('div[@class="product-iWrap"]/div[@class="productThumb clearfix"]/div[@class="proThumb-wrap"]/p[@class="ks-switchable-content"]/b'):  # extracts all <p> inside
                # print b.extract()
       
                item['colorskuid'+str(idx)] = self.getxpathvalue(b.xpath('./@data-sku').extract())
                item['colorimg'+str(idx)] = self.getxpathlink(b.xpath('./img/@src').extract())

                idx = idx + 1
                # item['img0'] = "https://" + b.xpath('/img@src').extract()
         
            yield item

    def getxpathvalue(self,selv):
        return str(selv).strip().strip('[]\'').strip()

    def getxpathlink(self,selv):
        tempstr = str(selv).strip().strip('[]\'').strip()
        if (not tempstr.startswith('http')):
            return "https:" + tempstr
        return tempstr
