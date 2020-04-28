'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 15:57:09
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-28 10:23:22
'''
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit
import sys

from pypinyin import pinyin
from .extract2 import IdiomPinyinMeaning

class AddIdioms(QDialog):
    def __init__(self,idioms:list=None):
        super(AddIdioms,self).__init__()

        self.setFixedSize(400,300)
        self.idioms = idioms

        self.idiom = QLabel("请输入成语：",self)
        self.idiomMeaning = QLabel("请输入成语释义：",self)

        self.idiomEdit = QLineEdit(self)
        self.idiomMeaningEdit = QTextEdit(self)


        self.idiom.move(20,20)
        self.idiomEdit.move(120,20)

        self.idiomMeaning.move(20,50)
        self.idiomMeaningEdit.move(120,50)

        self.idiomMeaningEdit.setPlainText("可不填")

        self.submit = QPushButton(self)
        self.submit.setText("提交")
        self.submit.clicked.connect(self.addIdioms)

        self.submit.move(170,260)
    
    def pylis2str(self,pylis:list):
        s = ""
        for i in pylis:
            s += i[0] + ' '
        return s


    
    def addIdioms(self):
        if self.idiomEdit.text().strip() == "":
            pass
        else:
            py = pinyin(self.idiomEdit.text().strip())
            start = py[0]
            end = py[-1]

            pystr = self.pylis2str(py)

            meaning = self.idiomMeaningEdit.toPlainText()

            iPYm = IdiomPinyinMeaning(self.idiomEdit.text().strip(),pystr, \
                meaning if meaning != "可不填" else "",start,end)
            
            if self.idioms is not None:
                self.idioms = list(set(self.idioms).add(iPYm))
            else:
                self.idioms = list(iPYm)
        
        self.close()
            # print(pystr)
            # print(meaning)
    
    @staticmethod
    def getData(parent=None):
        dialog = AddIdioms(parent)
        result = dialog.exec_()
        return dialog.idioms


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AddIdioms()
    demo.show()
    sys.exit(app.exec_())