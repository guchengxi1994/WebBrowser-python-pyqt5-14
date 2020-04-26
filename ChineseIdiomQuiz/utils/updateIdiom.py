'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-26 16:36:45
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-26 16:53:44
'''

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, \
    QPushButton, QHBoxLayout, QVBoxLayout,QDialog,QLabel,QLineEdit,QTextEdit
import sys

from pypinyin import pinyin
from .extract2 import IdiomPinyinMeaning
# from extract2 import IdiomPinyinMeaning

backupIdiomsPath = ""

class UpdateIdioms(QDialog):
    def __init__(self,idioms:list=None,thisIdiom:IdiomPinyinMeaning=None):
        super(UpdateIdioms,self).__init__()

        self.setFixedSize(400,300)
        self.idioms = idioms
        self.thisIdiom = thisIdiom

        self.idiom = QLabel("请输入成语：",self)
        self.idiomMeaning = QLabel("请输入成语释义：",self)

        self.idiomEdit = QLineEdit(self)
        self.idiomMeaningEdit = QTextEdit(self)


        self.idiom.move(20,20)
        self.idiomEdit.move(120,20)

        self.idiomMeaning.move(20,50)
        self.idiomMeaningEdit.move(120,50)

        if self.thisIdiom is not None:
            self.idiomEdit.setText(self.thisIdiom.idiom)
            self.idiomMeaningEdit.setPlainText(self.thisIdiom.meaning if self.thisIdiom.meaning.strip()!= "" else "可不填")
        else:
            self.idiomMeaningEdit.setPlainText("可不填")

        self.submit = QPushButton(self)
        self.submit.setText("提交")
        # self.submit.clicked.connect(self.addIdioms)

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
                pass

    
    def updateIdioms(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = UpdateIdioms()
    demo.show()
    sys.exit(app.exec_())