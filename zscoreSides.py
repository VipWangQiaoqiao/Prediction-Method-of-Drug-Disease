# coding: utf-8
import sys
import numpy as np
import pandas as pd
from sklearn import preprocessing
import networkx as nx
import xlrd
import random

sys.path.append("sideMain2.py")
import sideMain2


df1 = pd.read_csv(r"E:\bigdata\data\du.csv")

def gene_select(gene):
    row = int(df1[df1['ge'] == gene].index.values)  # 该基因所在行
    if row < 100:  # 这个基因前或后100个基因中随机挑
        g1 = df1.iloc[0:row + 100]
    elif row > 17605:
        g1 = df1.iloc[row - 100:17705]
    else:
        g1 = df1.iloc[row - 100:row + 100]
    g = int(g1.sample(n=1)['ge'])  # 随机选取一个基因数据，并转为int类型
    return g

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
#列表
G.add_edges_from(edgelist)                  #对于无向图，边3-2与边2-3被认为是一条边

model = sideMain2.xlsx_file.parse('Gene Vector', index_col='Gene')

def zscore():

    df = sideMain2.xlsx_file.parse('00Drug-Gene_Network')
    grouped = df.groupby('Drug')
    drug = []
    target = []
    for group in grouped.groups:
        drug.append(group)
        target.append(list(grouped.get_group(group)['Gene']))

    diseaseGene = sideMain2.research_diseaseGene('breast neoplasms')
    disease_gene = []
    for dG in diseaseGene:
        if np.int(dG) in model.iloc[:, 0]:
            disease_gene.append(np.int(dG))

    closest = []
    flg = 0
    for item in target:  # 2833
        print(flg)
        flg += 1
        closest1 = []
        for i in range(1000):
            num = len(item)
            distance = 0.0
            for ge in item:  # 30药物
                min_dis = 10
                if ge in model.iloc[:, 0]:
                    g1 = gene_select(ge)
                else:
                    num -= 1
                    if num == 0:
                        break
                    else:
                        continue
                for gene in disease_gene:
                    g2 = gene_select(gene)
                    # 提取本地基因与基因之间的边数
                    try:
                        t = nx.shortest_path_length(G, g1, int(g2))
                    except nx.NetworkXNoPath:
                        continue
                    min_dis = min(min_dis, t)

                if min_dis == 10:
                    num -= 1
                else:
                    distance = distance + min_dis

            if num == 0:
                closest1.append(np.NAN)
            else:
                closest1.append(distance / num)
            if num < 0:
                print("num<0")

        closest.append(closest1)
    df = pd.DataFrame(closest)
    df.to_csv('df_asthma.csv')


if __name__ == "__main__":
    zscore()
    df = pd.read_csv('df_asthma.csv', index_col=0)
    result = pd.DataFrame({'mean': pd.Series(df.mean(axis=1)), 'std': pd.Series(df.std(axis=1))})
    # result.to_csv('result_mean_std_asthma.csv')

    df1 = pd.read_csv('resultSide_breast neoplasms.csv')
    result = pd.concat([df1, result], axis=1)
    result.to_csv('6144-8515resultSide_breast neoplasms.csv')

    #df2 = pd.read_csv('resultSide_zscore_asthma.csv')
    #df2['zscore'] = (df2['distance'] - df2['mean']) / df2['std']
    #df2 = df2.sort_values(['zscore'])  # 升序
    #df2.to_csv('resultSide_zscore_asthma.csv')

