'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-16 15:40:21
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-17 15:46:43
'''
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,QFileDialog,QInputDialog,QMessageBox, \
    QCheckBox,QVBoxLayout,QHBoxLayout,QLabel,QDialog,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys,os,requests
from PyQt5.QtWebEngineWidgets import QWebEngineView
import utils.repath as repath
from utils.analyse import *
from utils.checkParams import CheckColumn


BASE_DIR = os.path.abspath(os.curdir)

if os.path.exists(BASE_DIR + '/static/net.txt'):
    with open(BASE_DIR + '/static/net.txt', 'r', encoding='utf-8') as data:
        defaultUrl = data.readline()
        # print(defaultUrl)
else:
    # import pathlib
    # pathlib.Path(BASE_DIR + '/static/net.txt').touch()
    f = open(BASE_DIR + '/static/net.txt','w',encoding='utf-8')
    defaultUrl = "https://www.bing.com"
    f.write(defaultUrl)
    f.close()
    


class UI(QMainWindow,):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle('Web browser')
        self.resize(1280,960)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + '/static/imgs/sun.png'))
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(self.main_toolbar)
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs_layout = QtWidgets.QGridLayout()
        self.tabs.setLayout(self.tabs_layout)
        self.url_edit = QtWidgets.QLineEdit()
        self.cwd = BASE_DIR + "/LocalWebTest/static/"

        self.ps = []
        
        self.browser = QWebEngineView()
        # Url = 'https://www.baidu.com'
        # Url = 'https://www.bing.com'
        Url = defaultUrl
        self.browser.setUrl(QtCore.QUrl(Url))
        self.tabs_layout.addWidget(self.browser)
        self.tabs.addTab(self.browser,'')
        self.browser.loadFinished.connect(lambda :self.tabs.setTabText(0,self.browser.page().title()))
        self.setCentralWidget(self.tabs)



        self.turn_button = QAction(QIcon(BASE_DIR + '/static/imgs/zhuandao.png'),'Turn',self)
        self.back_button = QAction(QIcon(BASE_DIR + '/static/imgs/fanhui.png'),'Back',self)
        self.next_button = QAction(QIcon(BASE_DIR + '/static/imgs/tiaozhuan.png'),'Forward',self)
        self.stop_button = QAction(QIcon(BASE_DIR + '/static/imgs/close.png'),'Stop',self)
        self.reload_button = QAction(QIcon(BASE_DIR + '/static/imgs/shuaxin.png'),'Reload',self)
        self.add_button = QAction(QIcon(BASE_DIR + '/static/imgs/add.png'),'Addpage',self)

        self.set_default_openPage_button = QAction(QIcon(BASE_DIR + '/static/imgs/lock.png'),'SetDefault',self)
        self.set_data_button = QAction(QIcon(BASE_DIR + '/static/imgs/data.png'),'AnalyzeData',self)



        self.main_toolbar.addAction(self.back_button)
        self.main_toolbar.addAction(self.next_button)
        self.main_toolbar.addAction(self.stop_button)
        self.main_toolbar.addAction(self.reload_button)
        self.main_toolbar.addAction(self.add_button)
        self.main_toolbar.addWidget(self.url_edit)
        self.main_toolbar.addAction(self.turn_button)

        self.main_toolbar.addAction(self.set_default_openPage_button)
        self.main_toolbar.addAction(self.set_data_button)
        



        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.close)
        self.reload_button.triggered.connect(self.browser.reload)
        self.turn_button.triggered.connect(self.OpenUrlLine)
        self.browser.urlChanged.connect(self.setUrlLine)
        self.tabs.tabBarDoubleClicked.connect(self.NewPage)
        self.add_button.triggered.connect(self.NewPage)
        self.tabs.tabCloseRequested.connect(self.Closepage)


        self.set_default_openPage_button.triggered.connect(self.defaultPage)
        self.set_data_button.triggered.connect(self.anaData)

    


    def showDialog(self,options:list):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        panel = QLabel()
        # panel.setText("请选择：")
        self.dialog=QDialog()
        
        self.okBtn=QPushButton("确定")
        self.cancelBtn=QPushButton("取消")

        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        s = len(options)
        # self.cb1 = QCheckBox('全选')
        if s > 0:
            self.varDict = locals()
            self.varDict['self.c_all'] = QCheckBox('全选')
            self.varDict['self.c_all'].stateChanged.connect(self.change_all)
            # self.varDict['self.c_all'].move(20,20)
            vbox.addWidget(self.varDict['self.c_all'])
            height = 0
            
            for i in range(0,s):
                height = 20+(i+1)*20
                self.varDict['self.c_'+str(i)] = QCheckBox(options[i])
                self.varDict['self.c_'+str(i)].stateChanged.connect(self.stateClicked)
                # self.varDict['self.c_'+str(i)].move(30,height)
                vbox.addWidget(self.varDict['self.c_'+str(i)])


        self.dialog.resize(300,height+100)

        self.dialog.setWindowTitle("提示信息！")
         #okBtn.move(50,50)#使用layout布局设置，因此move效果失效
          # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

         #消息label与按钮组合纵向布局
        vbox.addWidget(panel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        self.dialog.setWindowModality(Qt.ApplicationModal)#该模式下，只有该dialog关闭，才可以关闭父界面


        # for i,j in self.varDict.items():
        #     print(i)
        #     print(j)
        self.dialog.exec_()


       #槽函数如下：
    def ok(self):
        print("确定保存！")
        self.dialog.close()
    def cancel(self):
        print("取消保存！")
        self.dialog.close()

    
    def change_all(self):
        ss = set()
        if self.varDict['self.c_all'].checkState() == Qt.Checked:
            for i,j in self.varDict.items():

                if  not  i.startswith('self.c_'):
                    continue
                j.setChecked(True)
                ss.add(j.text() if j.text()!="全选" else None)
            ss = list(ss)
            self.ps = list(filter(None, ss)) 
            print(self.ps)
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
                ss.add(lp.text())       
        self.ps = list(ss)
        

        


    def anaData(self):
        # import time
        """
        数据分析
        """
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.txt)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        # print("\n你选择的文件为:")
        # print(fileName_choose)
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入需要分析的数据表名：')
        
        if ok:
            if text != "":               
                options = readColumn(fileName_choose,sheetName=text)
            else:
                QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
                options = readColumn(fileName_choose,sheetName='Sheet1')

                self.showDialog(options)

                
                # print(options)
                # ch = CheckColumn(options).sendData2()
                # while(ch == []):
                #     time.sleep(500)
                # print(ch)
                
                
                
        
        else:
            QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
            options = readColumn(fileName_choose,sheetName='Sheet1')


        
        




    def defaultPage(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入默认网址：')
        if ok :
            if text != "":
                # print(text)
                if repath.judge(text):
                    # print(text)
                    f = open(BASE_DIR+"/static/net.txt",'w',encoding='utf-8')
                    if str(text).startswith("http://") or str(text).startswith("https://"):
                        
                        f.writelines(text)
                    else:
                        f.writelines("http://"+text)
                    
                    f.close()
                else:
                    QMessageBox.critical(self, "错误对话框", "你输入网址模式错误", QMessageBox.Yes )
            else:
                QMessageBox.warning(self, "警告对话框", "你未输入网址", QMessageBox.Yes )


    def setUrlLine(self,url):
        self.url_edit.setText(url.toString())

    def OpenUrlLine(self):
        self.urlline = self.url_edit.text()
        print(self.urlline)
        # self.url_edit.setText(url_edit)
        self.browser.setUrl(QtCore.QUrl("http://" + self.urlline))

    def NewPage(self,url=defaultUrl,label=''):
        browser = QWebEngineView()
        # Url = 'https://cn.bing.com'
        Url = defaultUrl
        browser.setUrl(QtCore.QUrl(Url))
        i = self.tabs.addTab(browser,label)
        self.tabs.setCurrentIndex(i)
        print(i)

        browser.loadFinished.connect(lambda :self.tabs.setTabText(i,browser.page().title()))

    def Closepage(self,i):
        if self.tabs.count() == 1:  
            self.tabs.removeTab(i)
            self.NewPage()
        else:
            self.tabs.removeTab(i)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = UI()
    gui.show()
    sys.exit(app.exec_())