# -*- coding: utf-8 -*-
from b5c_automation.b5c_function.config import *
from b5c_automation.b5c_function.public import *
from b5c_automation.b5c_elements.mainpage_elements import *
from selenium import webdriver
import logging


class MainPage:
    def __init__(self, dr):
        self.dr = dr
        self.element = GetElements(self.dr)
        self.f = Function(self.dr)
        Config().log_conf()

    def login(self, account, password):
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

    def cls(self):
        if self.dr:
            self.dr.quit()
            self.dr = None
