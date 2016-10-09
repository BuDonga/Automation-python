#-*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
from b5c_testcase import login, payment
from b5c_function.config import *
from b5c_automation.b5c_function.public import *

if __name__ == '__main__':
    """切换到case路径"""
    os.chdir('b5c_testcase\\')

    """删除当天目录下的截图文件"""
    #Function.delete_snapshot()

    """需要跑的case"""
    allCases = [
        login.Login,
        payment.Payment
    ]
    testUnit = unittest.TestSuite()
    for s in allCases:
        testUnit.addTest(unittest.makeSuite(s))

    """设置文件名格式及路径"""
    filename = ''.join(('TestReport_', time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime()), '.html'))
    filePath = ''.join(('..\\report\\', filename))
    fp = file(filePath, 'wb')

    """设置报告格式，并生成"""
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'帮5采自动化测试用例', description=u'用例运行情况')
    runner.run(testUnit)
    fp.close()
    print 'report is finished'

    """发送邮件"""
    a = Config()
    if a.send_mail():
        print "Sending OK!"
    else:
        print "Sending failed!"
