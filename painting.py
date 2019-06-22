# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlrd

# #计算所有药物的靶标个数，并生成numOfTarget.csv
# xlsx_file = pd.ExcelFile(r"E:\bigdata\data\Medical_Data.xlsx")
# df = xlsx_file.parse('Drug-Gene_Network')
# workbook = xlrd.open_workbook(r"E:\bigdata\data\Medical_Data.xlsx")
# Sheet1 = workbook.sheet_by_index(1)
# def numOfTarget(drug):
# 	n = 0
# 	for i in range(Sheet1.nrows):
# 		rows = Sheet1.row_values(i)
# 		if rows[0] == drug:
# 			n += 1
# 	return n
#
# drug=df['drugs'].tolist()
# num=[]  #存靶标数的列表
# for d in drug:
# 	num.append(numOfTarget(d))
# result=pd.DataFrame(drug,columns=['drug'])
# result = pd.concat([result, pd.DataFrame(num, columns=['numOfTarget'])], axis=1)
# df1 = result.sort_values(['numOfTarget'],ascending=0)
# df1.to_csv(r"E:\bigdata\data\numOfTarget.csv", index = False)

df=pd.read_csv(r"E:\bigdata\data\du.csv")
d=df['du'].tolist()
#均值
mean = np.mean(d)
#中位数
median = np.median(d)
print("mean = ", mean,"median = ", median)

# df=pd.read_csv(r"E:\bigdata\data\numOfTarget.csv")
# d=df['numOfTarget'].tolist()
# mean = np.mean(d)
# median = np.median(d)
# print("mean = ", mean,"median = ", median)
# 参数依次为list,抬头,X轴标签,Y轴标签,XY轴的范围
def draw_hist(d,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(d,9775)      #10000个竖条
    # plt.hist(d,258)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()
draw_hist(d,'Gene Information','Degree of gene','Number of gene',1,140,1,1400)   # 直方图展示
# draw_hist(d,'Drug-Target Information','Number of targets','Number of drugs',1,60,1,800)   # 直方图展示
#