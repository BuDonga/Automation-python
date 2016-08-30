# -*- coding: utf-8 -*-
from __future__ import with_statement
import ConfigParser
import time
import logging
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class Config:
    def __init__(self):
        self.config = ConfigParser.ConfigParser()

    def getValue(self, con, key):
        """取得配置文件的值"""
        with open(r'..\sys.conf', 'r') as cfgfile:
            self.config.readfp(cfgfile)
        value = self.config.get(con, key)
        return value

    def setValue(self, con, key, value):
        """设置配置文件的值，如果没有，则创建"""
        with open(r'..\sys.conf', 'r') as cfgfile:
            self.config.readfp(cfgfile)
        try:
            self.config.set(con, key, value)
            cfgfile = open(r'..\sys.conf', 'r+')
            self.config.write(cfgfile)
        except Exception as e:
            print e
            self.config.add_section(con)
            self.config.set(con, key, value)
            cfgfile = open(r'..\sys.conf', 'w')
            self.config.write(cfgfile)
        finally:
            cfgfile.close()

    @staticmethod
    def log_conf():
        """设置log文件的存储路径"""
        log_name = ''.join(('AutoTest_', time.strftime('%Y%m%d', time.localtime()), '.log'))
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=os.path.join(os.getcwd(), '..\\log\\', log_name),
                            filemode='a')

    @staticmethod
    def send_mail():
        """发送邮件"""
        Config.log_conf()
        report_name = Config.get_newest_report()  # 得到最新生成的report名字
        mailto_list = 'guohuai@b5m.com'
        # mailto_list = ['guohuai@b5m.com', '595220635@qq.com']  # 收件组
        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "fish880111"  # 用户名
        mail_pass = "godda870910"  # 口令
        mail_postfix = "163.com"  # 发件箱的后缀
        me = u'郭淮' + "<" + mail_user + "@" + mail_postfix + ">"
        report_path = ''.join((r'../report/', report_name))
        try:
            with open(report_path) as f:
                content = f.read()
                print 'mail is sending...'
        except IOError, e:
            logging.error(e)
        # msg = MIMEText(content, 'html', _charset='utf-8')
        msg = MIMEMultipart()
        body = MIMEText(content, 'html', _charset='utf-8')
        msg.attach(body)

        '''添加html附件'''
        try:
            filename = ''.join(('..\\report\\', report_name))
            with open(filename) as ff:
                a = ff.read()
        except IOError, e:
            logging.error(e)
        att = MIMEApplication(a, _subtype="html")
        att.add_header('Content-Disposition', 'attachment', filename=report_name)
        msg.attach(att)

        '''设置标题、寄件人、收件人'''
        msg['Subject'] = Header('帮5采自动化测试报告', 'utf-8')
        msg['From'] = me
        # msg['To'] = ";".join(mailto_list)
        msg['To'] = mailto_list

        '''发邮件'''
        try:
            server = smtplib.SMTP()
            server.connect(mail_host, 25)
            server.login(mail_user, mail_pass)
            server.sendmail(me, mailto_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            logging.info(e)
            return False

    @staticmethod
    def get_newest_report():
        """根据创建时间排序，得到最新的测试报告
            a：获得report目录下所有文件的文件名
            c：创建一个字典，用来存储各文件的信息，key是创建时间（未经过时间戳处理），value是文件名
            b：用来遍历a目录下的文件名
            d：存储所有文件的创建时间，并且倒序排列，最新的创建时间是d[0]
            c[d[0]]:返回最新创建时间所对应的文件名，即是最新的测试报告
        """
        a = os.listdir(r'..\report')
        c = {}
        for b in a:
            c[os.stat(''.join(('..\\report\\', b))).st_atime] = b
            d = sorted(c.keys(), reverse=True)
        return c[d[0]]


if __name__ == '__main__':
    with open(r'..\report\TestReport_2016-08-17-16_25_29.html') as f:
        cont = f.read()
        print 'mail is sending...'
    if Config.send_mail("帮5采自动化测试报告", cont):
        print "发送成功"
        logging.info('发送成功')
    else:
        print "发送失败"
        logging.info('发送失败')

# if __name__ == '__main__':
#     print os.getcwd()
#     a = Config()
#     print 'haha'
#     b = a.getValue('Path', 'chrome_path')
#     print b
#     a.setValue('haha1ha','1223','gggd')
