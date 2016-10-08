# -*- coding: utf-8 -*-
import logging

import shutil
from selenium import webdriver
import config
import time
import os


class Function:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome()
        self.conf = config.Config()
        self.conf.log_conf()

    def get_snapshot(self, filename):
        """
        在snapshot目录下存入snapshot，如果没有当前时间的目录，则创建，反之，存入当前日期的目录
        """
        file_name = time.strftime('%Y%m%d', time.localtime())
        shapshot_name = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        files = os.listdir(r'../snapshot')
        if file_name not in files:
            os.mkdir(''.join(('../snapshot', '//', file_name)))
        self.driver.get_screenshot_as_file(''.join(('../snapshot', '//', file_name, '//', shapshot_name, '_', filename,
                                           '.png')))

    @staticmethod
    def delete_snapshot():
        """删除当天目录下的所有截图文件"""
        path_date = time.strftime('%Y%m%d', time.localtime())
        path = '..\\snapshot\\' + path_date + '\\'
        file_list = os.listdir(path)
        for file in file_list:
            file_path = ''.join((path, file))
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, True)

    def has_load_page_succeed(self, url):
        """初始化，并且登录url"""
        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(self.conf.getValue('Time', 'implicitly_wait'))
            self.driver.get(url)
            return True
        except Exception, e:
            logging.warn(u'******************本次启动WebDriver异常挂起******************')
            logging.warn(e)
            return False

    def driver_start(self, url, times):
        """
        启动浏览器，尝试多次启动
        :param url: 登录链接
        :param times: 启动次数
        :return: None
        """
        index = 0
        suspend = True
        while index < times & suspend:
            if index != 0:
                logging.warn(u'******************重载中!!!******************')
            suspend = not self.has_load_page_succeed(url)
            index += 1
        if index == times & suspend:
            raise RuntimeError(u'无法启动浏览器，请检查！！！')

    """定位单个元素封装"""
    def findId(self, id):
        return self.driver.find_element_by_id(id)

    def findName(self, name):
        return self.driver.find_element_by_name(name)

    def findCalssName(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def findTag(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def findLinkText(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def findPlinkText(self, plink_text):
        return self.driver.find_element_by_partial_link_text(plink_text)

    def findCss(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def findXpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    """定位多个元素封装"""
    def findsId(self, id):
        return self.driver.find_elements_by_id(id)

    def findsName(self, name):
        return self.driver.find_elements_by_name(name)

    def findsCalssName(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)

    def findsTag(self, tag_name):
        return self.driver.find_elements_by_tag_name(tag_name)

    def findsLinkText(self, link_text):
        return self.driver.find_elements_by_link_text(link_text)

    def findsPlinkText(self, pLink_text):
        return self.driver.find_elements_by_partial_link_text(pLink_text)

    def findsCss(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    def findsXpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)


if __name__ == '__main__':
    dr = webdriver.Chrome()
    a = Function(dr)
