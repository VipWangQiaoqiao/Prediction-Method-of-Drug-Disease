#coding=utf-8
import pandas as pd
import numpy as np
import re
import xlrd
import networkx as nx
from itertools import combinations

gen=pd.read_csv(r"E:\bigdata\data\gene.csv")
gen.index=gen['Gene']
# 数据导入，预处理
edgelist = []
def open_excel(file):
    try:
        sheet_data = xlrd.open_workbook(file)
        return sheet_data
    except Exception as e:
        print(str(e))

def praise_excel(file):
    sheet_data = open_excel(file)
    sheet = sheet_data.sheets()[0]    #读取sheet
    my_queues0 = sheet.col_values(0)   #读取1列
    my_queues1 = sheet.col_values(1)   #读取2列
    for i, j in zip(my_queues0,my_queues1):
        x = (int(i),int(j))
        edgelist.append(x)

praise_excel(r"E:\bigdata\data\Human Interactome_201706.xlsx")
G=nx.Graph() #创建了一个没有节点和边的空图
G.add_edges_from(edgelist)                  #对于无向图，边3-2与边2-3被认为是一条边

def numOfSides(p,q):
    try:
        n=nx.shortest_path_length(G,p,q)
    except nx.NetworkXNoPath:
        n=np.NAN
    return n

side=pd.DataFrame(index=list(gen.index),columns=list(gen.index) )
for gen_light in combinations(gen.index, 2):
    side[gen_light[1]].ix[gen_light[0]]=side[gen_light[0]].ix[gen_light[1]]=numOfSides(gen_light[0],gen_light[1])

side.to_csv(r"E:\bigdata\data\side.csv")
result=pd.read_csv(r"E:\bigdata\data\side.csv")
print(result.tail())