# -*- coding: utf-8 -*-

import os
import time
source = ['/test11']
target_dir = '/test22'
today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime('%H%M%S')
touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "zip -qr " + touch + ' ' + ' '.join(source)


if os.path.exists(today_dir) == 0:
    os.mkdir(today_dir)
if os.system(command_touch) == 0:
    print 'Success'
else: print 'Failed'
