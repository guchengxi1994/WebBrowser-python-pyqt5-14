'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:58:31
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-21 15:31:21
'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
from pandas import DataFrame
import random
from .pltType import *

colors = list(cnames.keys())

def readColumn(path:str,sheetName):
    params = []
    if os.path.exists(path):
        try:
            df = pd.read_excel(path,sheetName)
            # print(df)
            # sns.violinplot(df[])
        except Exception:
            # raise SheetNotFoundError("表不存在")
            return []
        # finally:
            # return params

        
        try:
            for column in df:
                params.append(column)
            return params
        except Exception:
            # raise SheetReadError("数据表读取错误")
            return []
        # finally:
        #     return []

    else:
        return params
        # pass

    
def plotFigure(path:str,sheetName:str,column:list=[],figure:str=""):
    df = pd.read_excel(path,sheetName)
    # print(df)
    d = []
    if len(column)>0:
        for i in column:
            d.append(df[i])
        # sns.lineplot(data=d)
        sns.lineplot(data=df)
        sns.despine()
            # filePath = path.split('/')
        filePath = os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir))
            # print(filePath)
        figurePath = filePath + os.sep + 'static'+os.sep +"test.png"
            # plt.show()
        if  os.path.exists(figurePath):
            os.remove(figurePath)
        plt.savefig(figurePath, bbox_inches='tight')
        # 参考 https://www.cnblogs.com/luoheng23/p/11050347.html
        plt.clf()
        return figurePath
                
    else:
        sns.lineplot(data=df)
        # sns.lineplot( data=df)
        sns.despine()
            # filePath = path.split('/')
        filePath = os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir))
            # print(filePath)
        figurePath = filePath + os.sep + 'static'+os.sep +"test.png"
            # plt.show()
        if  os.path.exists(figurePath):
            os.remove(figurePath)
        plt.savefig(figurePath, bbox_inches='tight')
        plt.clf()
        return figurePath
    


def plotFigureWithLabels(path:str,sheetName:str,columns:list=[],figure:str="",\
    xstick="",ystick=""):
    #for test
    # column = ['X','Y']
    df = pd.read_excel(path,sheetName)
    d = []
    if len(columns)>0:
        for i in columns:
            plt.plot(df[i],label=i,color=random.choice(colors),\
                ls=random.choice(linestyle),marker=random.choice(marker))
    else:
        columns = []
        # plt.plot(df)
        for column in df:
            columns.append(column)
        for i in columns:
            plt.plot(df[i],label=i,color=random.choice(colors),\
                ls=random.choice(linestyle),marker=random.choice(marker))
    plt.legend(loc=2)
    plt.xlabel(xstick)
    plt.ylabel(ystick)

    filePath = os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir))
    # print(filePath)
    figurePath = filePath + os.sep + 'static'+os.sep +"testAA.png"
    if  os.path.exists(figurePath):
        os.remove(figurePath)
    plt.savefig(figurePath, bbox_inches='tight')
    plt.clf()
    return figurePath
    # plt.show()
    
    # print(d)

    



        



if __name__ == "__main__":
    
    path = "D:/testALg/WebBrowser-python-pyqt5-14/LocalWebTest/static/data.xls"
    # p = readColumn(path,'Sheet2')
    # print(p)
    # plotFigure(path,'Sheet1')
    plotFigureWithLabels(path,'Sheet1')