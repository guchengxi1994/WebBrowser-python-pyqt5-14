'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-28 09:17:16
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-28 09:47:35
'''

import pickle
import os

class UserQuizResult(object):
    def __init__(self,username:str="guest",mode1=0,mode2=0,mode3=0,sumQuiz=0):
        self.username = username
        self.mode1 = mode1
        self.mode2 = mode2
        self.mode3 = mode3
        self.sumQuiz = sumQuiz

    def _update(self,mode1=0,mode2=0,mode3=0,sumQuiz=0):
        if mode1>self.mode1:
            self.mode1 = mode1
        if mode2 > self.mode2:
            self.mode2 = mode2
        if mode3 > self.mode3:
            self.mode3 = mode3
        if sumQuiz>self.sumQuiz:
            self.sumQuiz = sumQuiz

    def _save(self):
        parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), "."))   # for test
        # parent_Base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        savePath = parent_Base_dir + os.sep + "static" + os.sep+"users"+os.sep + self.username + ".pkl"
        
        u = UserQuizResult(self.username,self.mode1,self.mode2,self.mode3,self.sumQuiz)
        pk_file = open(savePath,'wb')
        pickle.dump(u,pk_file)
        pk_file.close()


        