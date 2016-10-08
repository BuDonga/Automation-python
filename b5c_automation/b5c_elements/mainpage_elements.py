# -*- coding: utf-8 -*-
from b5c_automation.b5c_function.public import *
from selenium import webdriver


class GetElements:

    def __init__(self, driver):
        self.element = Function(driver)

    def login_element(self):
        """登录按钮"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[1]/div/div[2]/div/a[1]')

    def account_element(self):
        """登录框"""
        return self.element.findXpath('//*[@id="loginform-username"]')

    def password_element(self):
        """密码框"""
        return self.element.findXpath('//*[@id="loginform-password"]')

    def login_btn(self):
        """登录按钮"""
        return self.element.findXpath('//*[@id="w0"]/ul/li[1]/button')

    def login_name_after(self):
        """登录完以后的用户名"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[1]/div/div[2]/div/span')

    def my_information(self):
        """我的帮5采"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[1]/div/div[1]/div/a[1]')

if __name__ == '__main__':
    a = GetElements('nihao', 99)
    print a.k
    print a.bbb()
