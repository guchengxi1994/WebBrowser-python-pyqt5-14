'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 09:23:41
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 09:33:38
'''

class SheetNotFoundError(Exception):
    def __init__(self,message):
        self.message = message

class SheetReadError(Exception):
    def __init__(self,message):
        self.message = message