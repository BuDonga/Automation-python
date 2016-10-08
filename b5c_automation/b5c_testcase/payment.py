# -*- coding: utf-8 -*-
import unittest
from b5c_automation.b5c_business.mainpage_business import *
from b5c_automation.b5c_business.payment_business import *
from b5c_automation.b5c_elements.my_information_elements import *
from b5c_automation.b5c_elements.mainpage_elements import *
import sys


class Payment(unittest.TestCase):
    def setUp(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.conf = Config()
        self.driver = webdriver.Chrome(self.conf.getValue('Path', 'chrome_path'))
        self.f = Function(self.driver)
        self.m = MainPage(self.driver)
        self.e = GetElements(self.driver)
        self.pay = PaymentBusiness(self.driver)
        self.base_url = self.conf.getValue('Path', 'base_url')
        self.f.driver_start(self.base_url, 3)

    def tearDown(self):
        self.m.cls()

    def test_payment_yijiandaifa_individual(self):
        u"""一件代发个人支付跳转"""
        self.m.login('15921826291', 'qq5566')
        time.sleep(2)
        try:
            if not self.assertEqual('awdadasd', self.e.login_name_after().text, '用户名不对'):
                print 'login is success'
                logging.info('login is success')
        except Exception, e:
            self.f.get_snapshot('not_login_success')
            logging.error(e)
            raise AssertionError

        """跳转我的帮5采"""
        self.m.my_b5c()
        if not self.assertEqual('http://b5cai.stage.com/myorder.html', self.driver.current_url, '我的资料没有跳转成功'):
            print '我的资料跳转成功'
            logging.info('我的资料跳转成功')
        else:
            logging.info('我的资料没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'我的资料没有跳转成功')
            raise AssertionError

        """进入待付款"""
        self.pay.to_be_payed()

        """获取相关订单数据"""
        ord_id = self.pay.get_order_id()
        print 'ord_id 是：%s' % ord_id
        payment_id = self.pay.get_payment_id()
        print '支付号是：%s' % payment_id

        """获取订单总金额"""
        total_amount = self.pay.get_total_amount()

        """获取待支付金额"""
        to_be_payed_amount = self.pay.get_to_be_payed_amount()
        if not to_be_payed_amount == total_amount:
            logging.error('订单总金额与待支付金额不同')
            self.f.get_snapshot('订单总金额与待支付金额不同')
            raise AssertionError

        """输入易汇金信息"""
        self.pay.login_yihuijin(u'李裕琪', u'310115198801110111')

        """获取易汇金金额"""
        yihuijin_amount = self.pay.get_yihuijin_amount()
        if not yihuijin_amount == total_amount:
            logging.error('易汇金金额与待支付金额不同')
            self.f.get_snapshot('易汇金金额与待支付金额不同')
            raise AssertionError

    def test_payment_yijiandaifa_enterprise(self):
        u"""一件代发企业支付跳转"""
        self.m.login('15921826291', 'qq5566')
        time.sleep(2)
        try:
            if not self.assertEqual('awdadasd', self.e.login_name_after().text, '用户名不对'):
                print 'login is success'
                logging.info('login is success')
        except Exception, e:
            self.f.get_snapshot('not_login_success')
            logging.error(e)
            raise AssertionError

        """跳转我的帮5采"""
        self.m.my_b5c()
        if not self.assertEqual('http://b5cai.stage.com/myorder.html', self.driver.current_url, '我的资料没有跳转成功'):
            print '我的资料跳转成功'
            logging.info('我的资料跳转成功')
        else:
            logging.info('我的资料没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'我的资料没有跳转成功')
            raise AssertionError

        """进入待付款"""
        self.pay.to_be_payed()

        """获取相关订单数据"""
        ord_id = self.pay.get_order_id()
        print 'ord_id 是：%s' % ord_id
        payment_id = self.pay.get_payment_id()
        print '支付号是：%s' % payment_id

        """获取订单总金额"""
        total_amount = self.pay.get_total_amount()

        """获取待支付金额"""
        to_be_payed_amount = self.pay.get_to_be_payed_amount()
        if not to_be_payed_amount == total_amount:
            logging.error('订单总金额与待支付金额不同')
            self.f.get_snapshot('订单总金额与待支付金额不同')
            raise AssertionError

        """进入企业支付"""
        self.pay.enterprise_enter()

        """获取易汇金金额"""
        yihuijin_amount = self.pay.get_yihuijin_amount()
        if not yihuijin_amount == total_amount:
            logging.error('易汇金金额与待支付金额不同')
            self.f.get_snapshot('易汇金金额与待支付金额不同')
            raise AssertionError

    def test_payment_qiugou_individual(self):
        u"""求购个人支付跳转"""
        self.m.login('15921826291', 'qq5566')
        time.sleep(2)
        try:
            if not self.assertEqual('awdadasd', self.e.login_name_after().text, '用户名不对'):
                print 'login is success'
                logging.info('login is success')
        except Exception, e:
            self.f.get_snapshot('not_login_success')
            logging.error(e)
            raise AssertionError

        """跳转我的帮5采"""
        self.m.my_b5c()
        if not self.assertEqual('http://b5cai.stage.com/myorder.html', self.driver.current_url, '我的资料没有跳转成功'):
            print '我的资料跳转成功'
            logging.info('我的资料跳转成功')
        else:
            logging.info('我的资料没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'我的资料没有跳转成功')
            raise AssertionError

        """我的求购进入支付选择页面"""
        amount = self.pay.my_purchase_payment()
        print amount[0], amount[1]
        my_purchase_amount = amount[0]  # 求购订单金额
        my_purchase_total_amount = amount[1]  # 合计金额
        if not my_purchase_amount == my_purchase_total_amount:
            logging.error('求购金额与总金额不同')
            self.f.get_snapshot('求购金额与总金额不同')
            raise AssertionError

        """输入易汇金信息"""
        self.pay.login_yihuijin(u'李裕琪', u'310115198801110111')

        """获取易汇金金额"""
        yihuijin_amount = self.pay.get_yihuijin_amount()
        if not yihuijin_amount == my_purchase_amount.split('￥')[1].replace(',', ''):  # 对求购订单金额格式进行处理，去除人民币符号以及逗号
            logging.error('易汇金金额与求购订单金额不同')
            self.f.get_snapshot('易汇金金额与求购订单金额不同')
            raise AssertionError

    def test_payment_qiugou_enterprise(self):
        u"""求购企业支付跳转"""
        self.m.login('15921826291', 'qq5566')
        time.sleep(2)
        try:
            if not self.assertEqual('awdadasd', self.e.login_name_after().text, '用户名不对'):
                print 'login is success'
                logging.info('login is success')
        except Exception, e:
            self.f.get_snapshot('not_login_success')
            logging.error(e)
            raise AssertionError

        """跳转我的帮5采"""
        self.m.my_b5c()
        if not self.assertEqual('http://b5cai.stage.com/myorder.html', self.driver.current_url, '我的资料没有跳转成功'):
            print '我的资料跳转成功'
            logging.info('我的资料跳转成功')
        else:
            logging.info('我的资料没有跳转成功，当前链接是%s' % self.driver.current_url)
            self.f.get_snapshot(u'我的资料没有跳转成功')
            raise AssertionError

        """我的求购进入支付选择页面"""
        amount = self.pay.my_purchase_payment()
        print amount[0], amount[1]
        my_purchase_amount = amount[0]  # 求购订单金额
        my_purchase_total_amount = amount[1]  # 合计金额
        if not my_purchase_amount == my_purchase_total_amount:
            logging.error('求购金额与总金额不同')
            self.f.get_snapshot('求购金额与总金额不同')
            raise AssertionError

        """进入企业支付"""
        self.pay.enterprise_enter()

        """获取易汇金金额"""
        yihuijin_amount = self.pay.get_yihuijin_amount()
        if not yihuijin_amount == my_purchase_amount.split('￥')[1].replace(',', ''):  # 对求购订单金额格式进行处理，去除人民币符号以及逗号
            logging.error('易汇金金额与求购订单金额不同')
            self.f.get_snapshot('易汇金金额与求购订单金额不同')
            raise AssertionError

if __name__ == '__main__':
    unittest.main()

