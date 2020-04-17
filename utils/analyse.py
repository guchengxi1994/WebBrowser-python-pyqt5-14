'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 08:58:31
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 15:20:12
'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
# from .myError import SheetNotFoundError
from .myError import SheetNotFoundError,SheetReadError
from PyQt5.QtWidgets import QWidget

def readColumn(path:str,sheetName):
    params = []
    if os.path.exists(path):
        try:
            df = pd.read_excel(path,sheetName)
            # print(df)
            # sns.violinplot(df[])
        except Exception:
            raise SheetNotFoundError("表不存在")
        

        try:
            for column in df:
                params.append(column)
            
        except Exception:
            raise SheetReadError("数据表读取错误")

    else:
        pass

    return params


        



# if __name__ == "__main__":
#     path = "D:/testALg/WebBrowser-python-pyqt5-14/LocalWebTest/static/data.xls"
#     ana(path,'Sheet1')