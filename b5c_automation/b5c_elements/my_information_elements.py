# -*- coding: utf-8 -*-
from b5c_automation.b5c_function.public import *


class MyInformationElements:
    def __init__(self, driver):
        self.element = Function(driver)

    def to_be_payed(self):
        """待付款"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[5]/div/div[2]/div[1]/a[2]')

    def pay(self):
        """立即支付(第一个订单)"""
        return self.element.findXpath('//*[@id="merge-pay-form"]/table[2]/tbody/tr/td[7]/div/a[1]')

    def pay_id(self):
        """支付id"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[2]/div[2]/div/div[1]/span')

    def user_name(self):
        """用户名"""
        return self.element.findXpath('//*[@id="pay-way-name"]')

    def user_id(self):
        """身份证号"""
        return self.element.findXpath('//*[@id="pay-way-card"]')

    def payment(self):
        """立即付款"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[3]/div/div[3]/span[1]')

    def order_amount(self):
        """订单总金额"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[2]/div[2]/div/div[2]/span')

    def to_be_payed_amount(self):
        """待付款金额"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[3]/div/div[3]/span[2]/b')

    def yihuijin_amount(self):
        """易汇金金额"""
        return self.element.findXpath('//*[@id="myTab"]/li[1]/span[2]')

    def enterprise_payment(self):
        """易汇金企业支付"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[3]/div/div[2]/div[2]/div[2]/img')

    def my_purchase(self, name):
        """左侧列表页"""
        elements = self.element.findsTag('dd')
        for element in elements:
            if element.text == name:
                return element




    def my_purchase_order_confirm(self):
        """我的求购订单确认（支付）"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[5]/div/div[2]/div[2]/div/div[1]/table[3]/tbody/tr/td[6]/a[1]')

    def my_purchase_amount(self):
        """求购订单金额"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[5]/div[4]/div/table/tbody/tr/td[5]/div/span')

    def my_purchase_total_amout(self):
        """合计金额"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[5]/div[4]/div/div[4]/div[1]/span[1]')

    def my_purchase_commit_order(self):
        """提交订单"""
        return self.element.findXpath('//*[@id="b5c_wrap"]/div[5]/div[4]/div/div[4]/div[2]')

