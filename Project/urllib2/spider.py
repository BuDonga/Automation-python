# -*- coding: utf-8 -*-

import re
import HTMLParser
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class GetReportData():
    def __init__(self, path, destination):
        self.path = path
        self.destination = destination

    def htmltrans(self, str):
        '''去除HTML转移符'''
        html_parser = HTMLParser.HTMLParser()
        return html_parser.unescape(str)

    def openfile(self):
        with open(self.path, 'r') as f:
            return f.read()

    def getdata(self, content):
        com = '<tr.*?<td>.*?>(.*?)</a>.*?<a href.*?>(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?' \
              '<td>(.*?)</td>'
        return re.findall(re.compile(com, re.S), content)

    def writeData(self, elements):
        f1 = open(self.destination, 'w')
        for i in elements:
            f1.write('test package name:%s\n\n' % i[0])
            f1.write('test case name:%s\n\n' % i[1])
            f1.write('test status:%s\n\n' % i[2])
            if i[3]:
                f1.write('log:%s\n\n' % self.htmltrans(i[3].replace('<br>', ''))
                         .replace('<code>', '').replace('</code>', ''))
            else:f1.write('log:%s\n\n' % 'Success, no log')
            f1.write('time duration:%s\n\n' % i[4])
            f1.write('-'*80+'\n')
        f1.close()


if __name__ == '__main__':
    fAccount = 0 #Failure的case数量
    eAccount = 0 #Error的case数量
    sAccount = 0 #Success的case数量
    total_time = 0 #总的test case运行情况
    tStatus = {'Failure': fAccount, 'Error': eAccount, 'Success': sAccount, 'Total_time': total_time}
    data = GetReportData(r'E:\Work\SVN\10.Product Mng\20.PPG\30.Development Mng'
                         r'\60.Automation\workspace\B5C\report\build\all-tests.html', r'E:\test_input.txt')
    fileContent = data.openfile()
    record = data.getdata(fileContent)
    data.writeData(record)
    for i in record:
        if i[2] == 'Failure':
            fAccount += 1
        elif i[2] == 'Error':
            eAccount += 1
        elif i[2] == 'Success':
            sAccount += 1
        total_time += float(i[4])
        tStatus['Failure'] = fAccount
        tStatus['Error'] = eAccount
        tStatus['Success'] = sAccount
        tStatus['Total_time'] = total_time
    print tStatus





