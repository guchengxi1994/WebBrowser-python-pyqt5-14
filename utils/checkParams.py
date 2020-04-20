'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 10:26:20
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-20 09:40:16
'''
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox, \
    QDialog,QCheckBox,QVBoxLayout,QHBoxLayout,QLabel,QDialog,QPushButton, \
    QDialogButtonBox,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt
import sys

class CheckColumn(QWidget):
    def __init__(self,columns:list):
        super().__init__()       
        self.columns = columns
        self.initUI()
        self.ps = []

    def initUI(self):
        #新建4个复选框对象
        s = len(self.columns)
        if s > 0:
            self.varDict = locals()
            self.varDict['self.c_all'] = QCheckBox('全选',self)
            self.varDict['self.c_all'].move(20,20)
            self.varDict['self.c_all'].stateChanged.connect(self.change_all)
            height = 0
            
            for i in range(0,s):
                # print(self.columns[i])
                height = 20+(i+1)*20
                self.varDict['self.c_'+str(i)] = QCheckBox(self.columns[i],self)
                self.varDict['self.c_'+str(i)].move(30,height)
                # self.cb1 = QCheckBox('全选',self)
                # self.cb2 = QCheckBox('你是',self)
                # self.cb3 = QCheckBox('我的',self)
                # self.cb4 = QCheckBox('宝贝',self)
                self.varDict['self.c_'+str(i)].stateChanged.connect(self.stateClicked)
                # self.QHBox_whole.addWidget(self.createVar['self.c_'+str(i)]);

            self.bt = QPushButton('提交',self) 
            self.bt.move(120,height+50)
            self.bt.clicked.connect(self.sendData)

        self.resize(300,height+100)
        self.show()
       

    def change_all(self):
        if self.varDict['self.c_all'].checkState() == Qt.Checked:
            for i,j in self.varDict.items():

                if i=='s' or i=='self':
                    continue
                j.setChecked(True)
                self.ps = self.columns
        else:
            for i,j in self.varDict.items():
                if i=='s' or i=='self':
                    continue
                j.setChecked(False)
                self.ps.clear()

    
    
    def stateClicked(self):
        ss = set()
        for i,j in self.varDict.items():
            
            if i=='s' or i=='self':
                continue
            lp=self.varDict[i]
            if lp.isChecked():
                ss.add(lp.text())
        
        self.ps = list(ss)
            
            # if lp.isChecked():
            # # self.ps.append(lp.text())
            #     print(lp.text())
            # print("================")
    
        # print(self.ps)

    def sendData(self):
        # from .params import CheckParam
        # CheckParam = self.ps
        self.close()
        # mySignal = pyqtSignal(list)
        # return self.ps
        # mySignal.emit(self.ps)

    def sendData2(self):
        return self.ps



class MyDialog_column_chosen(QDialog):
    def __init__(self,options,parent=None):
        super(MyDialog_column_chosen, self).__init__(parent)
        self.setWindowTitle('CheckBoxDialog')
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        # self.panel = QLabel(self)

        # self.dialog=QDialog()

        self.ps = []
        
        self.okBtn=QPushButton("确定")
        self.cancelBtn=QPushButton("取消")

        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        # buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, \
        #     Qt.Horizontal, self)

        # buttons.accepted.connect(self.accept)
        # buttons.rejected.connect(self.reject)

        s = len(options)
        # self.cb1 = QCheckBox('全选')
        if s > 0:
            self.varDict = locals()
            self.varDict['self.c_all'] = QCheckBox('全选')
            self.varDict['self.c_all'].stateChanged.connect(self.change_all)
            # self.varDict['self.c_all'].move(20,20)
            self.vbox.addWidget(self.varDict['self.c_all'])
            height = 0
            
            for i in range(0,s):
                height = 20+(i+1)*20
                self.varDict['self.c_'+str(i)] = QCheckBox(options[i])
                self.varDict['self.c_'+str(i)].stateChanged.connect(self.stateClicked)
                # self.varDict['self.c_'+str(i)].move(30,height)
                self.vbox.addWidget(self.varDict['self.c_'+str(i)])


        # self.dialog.resize(300,height+100)

        # self.dialog.setWindowTitle("提示信息！")
         #okBtn.move(50,50)#使用layout布局设置，因此move效果失效
          # 确定与取消按钮横向布局
        self.hbox.addWidget(self.okBtn)
        self.hbox.addWidget(self.cancelBtn)

         #消息label与按钮组合纵向布局
        # self.vbox.addWidget(self.panel)
        self.vbox.addLayout(self.hbox)


    
    def change_all(self):
        ss = set()
        if self.varDict['self.c_all'].checkState() == Qt.Checked:
            for i,j in self.varDict.items():

                if  not  i.startswith('self.c_'):
                    continue
                j.setChecked(True)
                ss.add(j.text() if j.text()!="全选" else None)
            sa = list(ss)
            self.ps = list(filter(None, sa)) 
            # print(self.ps)
        else:
            for i,j in self.varDict.items():
                if   not  i.startswith('self.c_'):
                    continue
                j.setChecked(False)
                self.ps = []

    
    
    def stateClicked(self):
        ss = set()
        for i,j in self.varDict.items():

            if not  i.startswith('self.c_'):
                continue
            lp=self.varDict[i]
            if lp.isChecked():
                ss.add(lp.text() if lp.text()!="全选" else None)  
            sa = list(ss)     
        self.ps = list(filter(None, sa)) 
    
    #槽函数如下：
    def ok(self):
        # print("确定保存！")
        self.close()
    def cancel(self):
        self.ps = []
        # print("取消保存！")
        self.close()

    @staticmethod
    def getData(options,parent=None):
        dialog = MyDialog_column_chosen(options,parent)
        result = dialog.exec_()
        return dialog.ps

    

class MyDialog_FigureType_chosen(QDialog):
    def __init__(self,parent=None):
        super(MyDialog_FigureType_chosen,self).__init__(parent)
        self.setWindowTitle('RadioBoxDialog')
        self.vbox = QVBoxLayout(self)
        # self.hbox = QHBoxLayout(self)

        self.info1 = ''

        self.rb1 = QRadioButton('折线图',self)
        self.rb2 = QRadioButton('饼图',self)
        self.rb3 = QRadioButton('柱状图',self)

        self.bt1 = QPushButton('提交',self)
        self.bt1.clicked.connect(self.ok)

        # self.bt1.move(20,120)

        self.vbox.addWidget(self.rb1)
        self.vbox.addWidget(self.rb2)
        self.vbox.addWidget(self.rb3)
        self.vbox.addWidget(self.bt1)

    

    def ok(self):
        # pass
        if self.rb1.isChecked():
            self.info1 = self.rb1.text()
        elif self.rb2.isChecked():
            self.info1 = self.rb2.text()
        else:
            self.info1 = self.rb3.text()
        
        self.close()

        # print(self.info1)




    @staticmethod
    def getData(options,parent=None):
        dialog = MyDialog_FigureType_chosen(parent)
        result = dialog.exec_()
        return dialog.info1

        





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckColumn(["X","Y","Z"])
    sys.exit(app.exec_())
