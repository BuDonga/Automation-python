# -*- coding:utf-8 -*-
import urllib2
import json


class FeeInquary:
    def __init__(self, ord_id,  url='http://i.b5cai.com/order/getorderbyid.json?orderId='):
        self.ord_id = ord_id
        self.url = ''.join((url, self.ord_id))

    def request(self):
        try:
            resp = urllib2.urlopen(self.url)
            content = json.loads(resp.read())
            return content
        except Exception:
            return 'Wrong Order ID, please enter again!'

    def get_pay_id(self):
        data = self.request()
        return str(data['data']['payId'])

if __name__ == '__main__':
    key = 1
    while(key):
        input_data = str(raw_input('Please enter Order ID: '))
        #input_data = 'b5cp476933011926', b5cp477461609681
        if input_data.lower() == 'exit':
            print 'Transaction is over'
            raise SystemExit
        a = FeeInquary(input_data)
        c = a.request()
        if c == 'Wrong Order ID, please enter again!':
            print c
            print '\n'
        else:
            key = 0
            b = a.get_pay_id()
            if b == 'None':
                print 'No Payment ID!'
            else:
                print 'Payment ID is: ' + b

