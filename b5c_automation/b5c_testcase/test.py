# -*- coding: utf-8 -*-
from __future__ import with_statement
import ConfigParser
import time
import logging
import os
import smtplib
from email.mime import application
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from b5c_function.config import *
import os

"""得到最新的Test Report"""
def get_newest_report():
    a = os.listdir(r'..\report')
    c = {}
    for b in a:
        c[os.stat(''.join(('..\\report\\', b))).st_atime] = b
        d = sorted(c.keys(), reverse=True)
    return c[d[0]]


if __name__ == '__main__':
    print get_newest_file()

# c = []
# for b in a:
#     c.append(b.split('TestReport_')[1].split('.html')[0])
# print c
# d = c.sort()
# e = c.reverse()
# print d
# print e
#
# os.stat()

