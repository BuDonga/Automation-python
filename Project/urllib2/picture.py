# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import savefig
from pylab import mpl

class ChatGeneration():
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    def __init__(self, pStatus):
        self.pStatus = pStatus

    def explode(self, label, target='Success'):
        '''选择需要重点显示的模块，默认是Success'''
        if label == target:
            return 0.1
        else:
            return 0

    def draw_table(self):
        col_labels = ['Success', 'Error', 'Failure', 'Total case', 'Total_time(s)']
        row_labels = ['']
        table_values = [[self.pStatus['Success'], self.pStatus['Error'], self.pStatus['Failure'], self.pStatus['Total'],
                         self.pStatus['Total_time']]]
        #row_colors = ['red', 'green', 'pink']
        plt.table(cellText=table_values,
                  colWidths=[0.1] * 5,
                  rowLabels=row_labels,
                  colLabels=col_labels,
                  #rowColours=row_colors,
                  loc='top')

    def pie_chart(self, hidden='yes'):
        if hidden == 'yes':
            matplotlib.use('Agg') #不显示图形
        labels = ['Success', 'Error', 'Failure']
        quants = [self.pStatus['Success'], self.pStatus['Error'], self.pStatus['Failure']]
        plt.figure(1, figsize=(6, 6)) #设置figure
        expl = map(self.explode, labels)
        colors = ["green", "red", "pink"] #设置图像的颜色
        plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=True) #设置饼图属性
        plt.title('Test Case Status Percentage', bbox={'facecolor': '0.8', 'pad': 5}) #设置标题
        savefig('pie_chart.jpg')
        plt.close()
        return plt

    def char_chart(self, hidden='yes'):
        if hidden == 'yes':
            matplotlib.use('Agg')  # 不显示图形
        labels = ['Success', 'Error', 'Failure','Total']
        quants = [self.pStatus['Success'], self.pStatus['Error'], self.pStatus['Failure'], self.pStatus['Total']]
        width = 0.4
        ind = np.linspace(0.5, 5.5, 4)
        fig = plt.figure(1, figsize=(12, 6)) #设置figure
        ax = fig.add_subplot(111)
        ax.bar(ind - width / 2, quants, width, color='coral') #设置bar
        ax.set_xticks(ind) #设置ticks
        ax.set_xticklabels(labels)
        ax.set_xlabel('Status')
        ax.set_ylabel('Test Case Amount')
        #ax.set_title('Test Case Status Percentage', bbox={'facecolor': '0.8', 'pad': 3}, loc='left')
        self.draw_table()
        savefig('char_chart.jpg')
        plt.close()
        return plt

if __name__ == '__main__':
    a = ChatGeneration({'Total_time': 129.716, 'Failure': 1, 'Success': 4, 'Error': 2, 'Total': 6})
    b = a.pie_chart()
    c = a.char_chart()
