# -*- coding: utf-8 -*-
from b5c_automation.b5c_function.config import *
from b5c_automation.b5c_elements.mainpage_elements import *
from b5c_automation.b5c_elements.my_information_elements import *
import logging


class PaymentBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.element = GetElements(self.driver)
        self.f = Function(self.driver)
        self.mie = MyInformationElements(self.driver)
        Config().log_conf()

    def is_exist(self, name, info):
        if not name:
            logging.info(info)
            self.f.get_snapshot(info)
            raise AssertionError

    def to_be_payed(self):
        """进入待付款"""
        self.mie.to_be_payed().click()
        time.sleep(2)
        self.mie.pay().click()
        time.sleep(2)
        logging.info('当前的url是：%s' % self.driver.current_url)
        if 'http://b5cai.stage.com/pay/way?ord=' not in self.driver.current_url:
            logging.info('支付选择页面没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'支付选择页面没有跳转成功')
            raise AssertionError

    def get_order_id(self):
        """得到order id"""
        ord_id = self.driver.current_url.split('ord=')[1]
        self.is_exist(ord_id, '没有找到order id')
        logging.info('order id是%s' % ord_id)
        return ord_id

    def get_payment_id(self):
        """得到支付号"""
        payment_id = self.mie.pay_id().text
        self.is_exist(payment_id, '没有找到支付id')
        logging.info('支付id是%s' % payment_id)
        return payment_id

    def get_total_amount(self):
        """获取订单总金额"""
        total_amount = self.mie.order_amount().text
        self.is_exist(total_amount, '没有找到订单金额')
        logging.info('订单总金额是%s' % total_amount)
        return total_amount

    def get_to_be_payed_amount(self):
        """获取待支付金额"""
        to_be_payed_amount = self.mie.order_amount().text
        self.is_exist(to_be_payed_amount, '没有找到待支付金额')
        logging.info('待支付总金额是：%s' % to_be_payed_amount)
        return to_be_payed_amount

    def login_yihuijin(self, account, password):
        """易汇金个人支付信息"""
        print self.driver.current_url
        time.sleep(2)
        self.mie.user_name().send_keys(account)
        self.mie.user_id().send_keys(password)
        self.mie.payment().click()
        time.sleep(2)
        print self.driver.current_url
        if 'cashier.ehking.com' not in self.driver.current_url:
            logging.error('易汇金跳转失败')
            self.f.get_snapshot(u'易汇金跳转失败')
            raise AssertionError

    def get_yihuijin_amount(self):
        """易汇金支付金额"""
        yihuijin_amount = self.mie.yihuijin_amount().text.split(' 人民币')[0]
        self.is_exist(yihuijin_amount, '没有找到易汇金支付金额')
        logging.info('易汇金金额是：%s' % yihuijin_amount)
        return yihuijin_amount

    def enterprise_enter(self):
        """点击易汇金企业支付"""
        self.mie.enterprise_payment().click()
        self.mie.payment().click()
        time.sleep(2)
        if 'cashier.ehking.com' not in self.driver.current_url:
            logging.error('易汇金跳转失败')
            self.f.get_snapshot(u'易汇金跳转失败')
            raise AssertionError

    def my_purchase_payment(self):
        """进入我的求购支付"""
        self.mie.my_purchase('我的求购').click()
        time.sleep(1)
        self.mie.to_be_payed().click()
        time.sleep(1)
        if 'http://b5cai.stage.com/begbuy.html?status=3' == self.driver.current_url:
            print '我的资料跳转成功'
            logging.info('我的资料跳转成功')
        else:
            logging.info('我的资料没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'我的资料没有跳转成功')
            raise AssertionError
        time.sleep(1)
        self.mie.my_purchase_order_confirm().click()
        time.sleep(1)
        my_purchase_amount = self.mie.my_purchase_amount().text
        my_purchase_total_amount = self.mie.my_purchase_total_amout().text
        self.mie.my_purchase_commit_order().click()
        # time.sleep(2)
        # if 'cashier.ehking.com' not in self.driver.current_url:
        #     logging.error('易汇金跳转失败')
        #     self.f.get_snapshot(u'易汇金跳转失败')
        #     raise AssertionError
        return [my_purchase_amount, my_purchase_total_amount]