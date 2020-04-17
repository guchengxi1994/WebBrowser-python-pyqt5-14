'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-17 10:26:20
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 16:38:34
'''
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox, \
    QDialog,QCheckBox,QVBoxLayout,QHBoxLayout,QLabel,QDialog,QPushButton, \
    QDialogButtonBox
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



class MyDialog(QDialog):
    def __init__(self,options,parent=None):
        super(MyDialog, self).__init__(parent)
        self.setWindowTitle('CheckBoxDialog')
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.panel = QLabel(self)

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
        self.vbox.addWidget(self.panel)
        self.vbox.addLayout(self.hbox)
        # self.dialog.setLayout(vbox)

        # self.dialog.setWindowModality(Qt.ApplicationModal)#该模式下，只有该dialog关闭，才可以关闭父界面

        # self.dialog.exec_()

    
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
        dialog = MyDialog(options,parent)
        result = dialog.exec_()
        return dialog.ps




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckColumn(["X","Y","Z"])
    sys.exit(app.exec_())
