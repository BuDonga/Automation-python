#-*- coding: UTF-8 -*-
import random


class pGame:
    def __init__(self):
        self.random_list = range(1, 10)

    def generate_random_list(self):
        """生成4位随机数，列表"""
        num_list = []
        for index in range(1, 5):
            num = random.choice(self.random_list)
            self.random_list.remove(num)
            num_list.append(num)
        return num_list

    def caculate_a(self, generate_list, input_value):
        a = 0
        for index in range(0, 4):
            if input_value[index] == str(generate_list[index]):
                a += 1
        return a

    def caculate_b(self, generate_list, input_value):
        b = 0
        for index in range(0, 4):
            if input_value[index] in str(generate_list):
                b += 1
        return b

if __name__ == '__main__':
    index = 8  # 尝试次数
    key = True
    c = pGame()
    random_list = c.generate_random_list()
    answer = ''.join(str(random_list))
    print answer
    while key:
        input_value = raw_input('Please enter 4 numbers differently, you only got %d chance:' %index)
        if len(input_value) < 4:
            print 'Input number is out of range, please enter again'
            continue
        if len(input_value) > 4:
            print 'Input number is out of range, please enter again'
            continue
        a = c.caculate_a(random_list, input_value)
        b = c.caculate_b(random_list, input_value) - a
        if a == 4:
            print 'Your answer is right!!!'
            break
        else:
            print 'a=%s' %a
            print 'b=%s' %b
            index = index - 1
            if index == 0:
                print 'Game is over!!! Answer is %s' %answer
                key = False

