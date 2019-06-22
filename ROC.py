# -*- coding: utf-8 -*-
import pylab as pl
import pandas as pd
import xlrd

drug_info=open("result_adenocarcinoma.csv","r")
dnum=len(drug_info.readlines())
print(dnum)

workbook=xlrd.open_workbook(r"E:\bigdata\data\summary sheet.xls")
sheet1_name=workbook.sheet_names()[0]
sheet1=workbook.sheet_by_index(0)
#sheet1=workbook.sheet_by_name('known drug-disease associations')
print(sheet1.name,sheet1.nrows,sheet1.ncols)

# disease='adenocarcinoma'
disease='epilepsy'
num=0
drug=[]
for i in range(sheet1.nrows):
    if sheet1.row(i)[0].value==disease:
        num+=1
        drug.append(sheet1.cell(i,2).value)
        if sheet1.row(i+1)[0].value!=disease:
            break
print(num,drug)

#¼ÆËãROC×ø±êµã
xy_arr=[]
j=0
csv=pd.read_csv("result_adenocarcinoma.csv",encoding='utf-8')
csv.to_excel("result_adenocarcinoma.xlsx",sheet_name='result')
df=xlrd.open_workbook("result_adenocarcinoma.xlsx")
data=df.sheet_by_index(0)

for i in range(dnum):
    if data.row(i)[2].value in drug:
        #print data.row(i)[2].value
        j+=1
    xy_arr.append([float(i)/(dnum-1),float(j)/num])
#print xy_arr

#¼ÆËãÇúÏßÏÂÃæ»ý
auc = 0.
prev_x = 0
for x,y in xy_arr:
    if x != prev_x:
        auc += (x - prev_x) * y
        prev_x = x

print("the auc is %s."%auc)

x = [_v[0] for _v in xy_arr]
y = [_v[1] for _v in xy_arr]
pl.title("ROC curve of %s (AUC = %.4f)" % (disease,auc))
pl.xlabel("False Positive Rate")
pl.ylabel("True Positive Rate")
pl.plot(x, y)# use pylab to plot x and y
pl.show()# show the plot on the screen