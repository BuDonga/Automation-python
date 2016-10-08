# -*- coding: utf-8 -*-
from b5c_automation.b5c_function.config import *
from b5c_automation.b5c_elements.mainpage_elements import *
import logging


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.element = GetElements(self.driver)
        self.f = Function(self.driver)
        self.e = GetElements(self.driver)
        Config().log_conf()

    def login(self, account, password):
        """登录"""
        try:
            self.element.login_element().click()
            self.element.account_element().send_keys(account)
            logging.info(''.join(('account is:', account)))
            self.element.password_element().send_keys(password)
            logging.info(''.join(('password is:', password)))
            self.element.login_btn().click()
        except Exception, e:
            logging.info(e)
            self.f.get_snapshot('Login')
            raise AssertionError

    def my_b5c(self):
        self.e.my_information().click()
        time.sleep(2)
        logging.info('当前的url是：%s' % self.driver.current_url)

    def cls(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        logging.info('=' * 30)
        logging.info('\n' * 2)

