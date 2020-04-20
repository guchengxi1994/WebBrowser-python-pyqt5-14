'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-16 15:40:21
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-20 13:41:45
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

        # self.ps = []
        
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
        
        #DIY
        self.set_default_openPage_button = QAction(QIcon(BASE_DIR + '/static/imgs/lock.png'),'SetDefault',self)
        self.set_data_button = QAction(QIcon(BASE_DIR + '/static/imgs/data.png'),'AnalyzeData',self)
        self.set_test_button = QAction(QIcon(BASE_DIR + '/static/imgs/test.png'),'TestButton',self)



        self.main_toolbar.addAction(self.back_button)
        self.main_toolbar.addAction(self.next_button)
        self.main_toolbar.addAction(self.stop_button)
        self.main_toolbar.addAction(self.reload_button)
        self.main_toolbar.addAction(self.add_button)
        self.main_toolbar.addWidget(self.url_edit)
        self.main_toolbar.addAction(self.turn_button)


        #DIY
        self.main_toolbar.addAction(self.set_default_openPage_button)
        self.main_toolbar.addAction(self.set_data_button)
        self.main_toolbar.addAction(self.set_test_button)
        



        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.close)
        self.reload_button.triggered.connect(self.browser.reload)
        self.turn_button.triggered.connect(self.OpenUrlLine)
        self.browser.urlChanged.connect(self.setUrlLine)
        self.tabs.tabBarDoubleClicked.connect(self.NewPage)
        self.add_button.triggered.connect(self.NewPage)
        self.tabs.tabCloseRequested.connect(self.Closepage)

        #DIY
        self.set_default_openPage_button.triggered.connect(self.defaultPage)
        self.set_data_button.triggered.connect(self.anaData)
        self.set_test_button.triggered.connect(self.test)

    
    def showDialog(self,options:list):
        from utils.checkParams import MyDialog_column_chosen
        from utils.checkParams import MyDialog_FigureType_chosen
        if len(options)>0:
            dialog_column = MyDialog_column_chosen(options)
            result = dialog_column.exec_()
            if len(dialog_column.ps)>0 :
                # print(dialog_column.ps)
                dialog_figureType = MyDialog_FigureType_chosen()
                retult = dialog_figureType.exec_()              
                return dialog_column.ps,dialog_figureType.info1
            else:
                dialog_figureType = MyDialog_FigureType_chosen()
                retult = dialog_figureType.exec_()              
                return options,dialog_figureType.info1
        else:
            QMessageBox.critical(self, "错误对话框", "表名错误或者为空表", QMessageBox.Yes )
            return [],""

       




    def test(self):
        # import requests
        url = 'http://localhost:5000/showImg'
        # self.OpenUrlLine(url)
        
        # data = {'imgName':'D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\test.png'}
        img = '?imgName=D:\\testALg\\WebBrowser-python-pyqt5-14\\LocalWebTest\\static\\test.png'
        self.browser.setUrl(QtCore.QUrl( url+img))
        # requests.post(url=url,data=data)
        
        # pass
        # from utils.checkParams import MyDialog_FigureType_chosen
        # dialog = MyDialog_FigureType_chosen()
        # retult = dialog.exec_()
        # print(dialog.info1)
        


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
                sheetName = text
                # print(text)          
                options = readColumn(fileName_choose,sheetName=text)
                ps,formType = self.showDialog(options)
            else:
                sheetName = 'Sheet1'
                QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
                options = readColumn(fileName_choose,sheetName='Sheet1')
                # print(options)
                # self.showDialog(options)
                ps,formType = self.showDialog(options)
        else:
            sheetName = 'Sheet1'
            QMessageBox.warning(self, "警告对话框", "将使用默认的\'Sheet1\'作为分析表", QMessageBox.Yes )
            options = readColumn(fileName_choose,sheetName='Sheet1')
            ps,formType = self.showDialog(options)
        
        

        



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
        if self.urlline.startswith('http://') or self.urlline.startswith('https://'):
            self.browser.setUrl(QtCore.QUrl( self.urlline))
        else:
            self.browser.setUrl(QtCore.QUrl( "http://" +self.urlline))


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