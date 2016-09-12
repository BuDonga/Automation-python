# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import logging
from b5c_automation.b5c_function.config import *
from b5c_automation.b5c_function.public import *
from b5c_automation.b5c_business.mainpage_business import *
from b5c_automation.b5c_elements.mainpage_elements import *


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
        self.conf = Config()
        self.f = Function(self.driver)
        self.m = MainPage(self.driver)
        self.e = GetElements(self.driver)
        self.conf.log_conf()
        self.base_url = "http://b5cai.stage.com/"
        self.f.driver_start(self.base_url, 3)

    def tearDown(self):
        self.m.cls()

    def test_login(self):
        self.m.login('15921826291', 'qq5566')
        try:
            if not self.assertEqual('awdadasd', self.e.login_name_after().text, '用户名不对'):
                print 'login is success'
                logging.info('login is success')
        except Exception, e:
                self.f.get_snapshot('not_login_success')
                logging.error(e)
                raise AssertionError


if __name__ == '__main__':
    unittest.main()

