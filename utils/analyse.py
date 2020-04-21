'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:58:31
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-21 10:46:44
'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
# from myError import SheetNotFoundError,SheetReadError
# from .myError import SheetNotFoundError,SheetReadError
# from PyQt5.QtWidgets import QWidget

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
    d = []
    if len(column)>0:
        for i in column:
            d.append(df[i])
        sns.lineplot( data=d)
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
                
    else:
        sns.lineplot( data=df)
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
    



        



if __name__ == "__main__":
    
    path = "D:/testALg/WebBrowser-python-pyqt5-14/LocalWebTest/static/data.xls"
    # p = readColumn(path,'Sheet2')
    # print(p)
    plotFigure(path,'Sheet1')
    plotFigure(path,'Sheet1')