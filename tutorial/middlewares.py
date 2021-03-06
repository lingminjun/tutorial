# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time
import weakref


class TutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TutorialDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # scroll_step = 0

    def __init__(self, timeout=None, service_args=[]):
        # self.driver.implicitly_wait(10) #   设置智能等待10秒
        # self.timeout = timeout
        # self.browser = webdriver.PhantomJS(service_args=service_args)
        # self.browser.set_window_size(1400, 700)
        # self.browser.set_page_load_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser, self.timeout)
        pass


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        print('self.wait.until is load html')

        driver = webdriver.Chrome('/Users/lingminjun/chromedriver/chromedriver')
    
        # self.browser.get(request.url)
        driver.get(request.url)

        # 打开页面后，滑动至页面底部
        return self.scroll_until_loaded(request, spider, driver)

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    #  模拟浏览器页面滚到页面底部的行为
    def scroll_until_loaded(self, request, spider, driver):
        # check_height = self.driver.execute_script("return document.body.scrollHeight;")
        # print("页面已经加载完成。高度为" + str(check_height))
        driver.implicitly_wait(2)

        wait = WebDriverWait(driver, 20)    # 30秒后超时
        step = StepItem(driver)

        while True:
            step.execute_scroll_step()
            try:
                # WebDriverWait(browser, 2).until(
                #         lambda driver: driver.find_element_by_tag_name('body'))
                wait.until(lambda driver: step.execute_scroll_step() )
                break
            except TimeoutException:
                break
            
        return HtmlResponse(url=request.url, body=driver.page_source, request=request, encoding='utf-8', status=200)
            
    
class StepItem():
    scroll_step = 0

    def __init__(self, driver):
        self.driver = driver

    def __del__(self):
        self.driver.close()

    def execute_scroll_step(self):
        self.scroll_step = self.scroll_step + 200   # 每次滚动200像素
        self.driver.execute_script("window.scrollTo(0, " + str(self.scroll_step) + ");")
        height = self.driver.execute_script("return document.body.scrollHeight;")
        print("height="+str(height) + "; step=" + str(self.scroll_step))
        return self.scroll_step > height + 100
