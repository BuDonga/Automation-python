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
import os
import shutil




if __name__ == '__main__':
    pass
    # path_date = time.strftime('%Y%m%d', time.localtime())
    # path = '..\\snapshot\\' + path_date + '\\'
    # file_list = os.listdir(path)
    # for file in file_list:
    #     print file
    #     file_path = ''.join((path, file))
    #     print file_path
    #     if os.path.isfile(file_path):
    #         os.remove(file_path)
    #     elif os.path.isdir(file_path):
    #         shutil.rmtree(file_path, True)


