#-*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
from b5c_automation.b5c_testcase import login, test_unittest
from b5c_automation.b5c_function.config import *

if __name__ == '__main__':
    '''需要跑的case'''
    allcases = [
        login.Login,
        test_unittest.Baidu
    ]
    testunit = unittest.TestSuite()
    for s in allcases:
        testunit.addTest(unittest.makeSuite(s))

    '''设置文件名格式及路径'''
    filename = ''.join(('TestReport_', time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime()), '.html'))
    filepath = ''.join(('report\\', filename))
    fp = file(filepath, 'wb')

    '''设置报告格式，并生成'''
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'帮5采自动化测试用例', description=u'用例运行情况')
    runner.run(testunit)
    print 'report is finished'

    '''发送邮件'''
    os.chdir('b5c_testcase')
    if Config.send_mail():
        print "Sending OK!"
    else:
        print "Sending failed!"
