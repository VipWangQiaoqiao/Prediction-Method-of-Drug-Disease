# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#数据
# df = pd.read_excel(r"E:\bigdata\data\InfoData.xlsx", usecols=[1,2,3], names=None)
# df_li = df.values.tolist()
# y1 = [_v[0] for _v in df_li]
# y2 = [_v[1] for _v in df_li]
# y3 = [_v[2] for _v in df_li]
# # df = pd.DataFrame({'一班':np.random.randint(1,100,N),
# #                    '二班':np.random.randint(1,100,N),
# #                    '三班':np.random.randint(1,100,N) })
# df = pd.DataFrame({'向量最近法':y1,
#                    '向量平均法':y2,
#                    '边数最近法':y3})
# #折线图
# df.plot()
# myfont = fm.FontProperties(fname=r'C:\Users\The Final Fantasy\Downloads\ukai.ttc')
# plt.legend(prop=myfont)
# plt.xlabel("Disease number")
# plt.ylabel("AUC")
# #柱状图
# df.plot(kind='bar')
# plt.legend(prop=myfont)
# plt.xlabel("Disease number")
# plt.ylabel("AUC")
# #热力图
# plt.figure()
# sns.heatmap(df)
# plt.xticks(fontproperties='STKAITI')
# #显示图形
# plt.show()

#柱状图
# 显示高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.1, 1.01*height, '%s' % int(height))

name_list = ['ClosestVector(dcv)', 'ShortestVector(dsv)', 'ClosestSide(dcs)']
num_list = [65, 62, 61]
autolabel(plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list,width=0.3))
plt.ylabel("AUC(%)")
plt.show()

#41种疾病的图
# workbook=xlrd.open_workbook(r"E:\bigdata\data\InfoData.xlsx")
# table = workbook.sheets()[2]  #在workbook这个变量中获取第三个sheet中的数据存与变量table中
# y1 = table.col_values(1)#读取第二列的值，并将列的值存变量y1中
#公共部分
# df = pd.read_excel(r"E:\bigdata\data\InfoData.xlsx", usecols=[1,2,3], names=None)
# df_li = df.values.tolist()
# x = range(1,36)
# y1 = [_v[0] for _v in df_li]
# y2 = [_v[1] for _v in df_li]
# y3 = [_v[2] for _v in df_li]
#散点图
# plt.scatter(x,y1)
# plt.scatter(x,y2)
# plt.scatter(x,y3)
# plt.legend(['dcv','dav','dcs'])
# plt.xlabel("disease")
# plt.ylabel("AUC")
# plt.show()
#折线图
# plt.figure()
# plt.ylim(0.2,1.)
# plt.plot(x,y1,'--x')
# plt.plot(x,y2,'-->')
# plt.plot(x,y3,'--b^')
# plt.xlabel("disease")
# plt.ylabel("AUC")
# plt.legend(['dcv','dav','dcs'])
# plt.show()