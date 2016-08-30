#-*- coding: UTF-8 -*-
import unittest

from selenium import webdriver


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []

    def tearDown(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def test_baidu(self):
        u"""百度测试3"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()

    def test_baidu2(self):
        u"""百度测试4"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw11").send_keys("sdfsdfsdfs")
        driver.find_element_by_id("su").click()

if __name__ == '__main__':
    unittest.main()