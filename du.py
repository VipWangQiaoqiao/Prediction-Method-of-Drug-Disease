#coding: utf-8
import pandas as pd
import xlrd

#度的计算
workbook = xlrd.open_workbook(r"E:\bigdata\data\Human Interactome_201706.xlsx")
Sheet1 = workbook.sheet_by_index(0)  # 获取一个工作表：通过索引顺序获取

def degree_num(num):
	h1 = 0
	h2 = 0

	for i in range(Sheet1.nrows):
		rows = Sheet1.row_values(i)
		if rows[0] == num:
			h1 += 1
		if rows[1] ==num:
			h2 += 1
	return h1+h2

#计算所有基因节点的度
xlsx_file = pd.ExcelFile(r"E:\bigdata\data\Medical_Data.xlsx")
df = xlsx_file.parse('Gene Vector')
# gene=[]

gene=df['Gene'].tolist()

n=[]  #存节点度的列表
for g in gene:
	n.append(degree_num(g))

result=pd.DataFrame(gene,columns=['ge'])
result = pd.concat([result, pd.DataFrame(n, columns=['du'])], axis=1)
df1 = result.sort_values(['du'],ascending=0)
df1.to_csv(r"E:\bigdata\data\du.csv", index = False)




