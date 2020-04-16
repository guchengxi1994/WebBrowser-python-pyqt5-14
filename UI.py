'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-16 15:40:21
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-16 17:07:37
'''
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,requests
from PyQt5.QtWebEngineWidgets import *
import utils.repath as repath


class UI(QMainWindow,):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle('Web browser')
        self.resize(680,480)
        self.setWindowIcon(QtGui.QIcon('./imgs/liulanqi.png'))
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16,16))
        self.addToolBar(self.main_toolbar)
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs_layout = QtWidgets.QGridLayout()
        self.tabs.setLayout(self.tabs_layout)
        self.url_edit = QtWidgets.QLineEdit()


        self.browser = QWebEngineView()
        # Url = 'https://www.baidu.com'
        Url = 'https://www.bing.com'
        self.browser.setUrl(QtCore.QUrl(Url))
        self.tabs_layout.addWidget(self.browser)
        self.tabs.addTab(self.browser,'')
        self.browser.loadFinished.connect(lambda :self.tabs.setTabText(0,self.browser.page().title()))
        self.setCentralWidget(self.tabs)



        self.turn_button = QAction(QIcon('./imgs/zhuandao.png'),'Turn',self)
        self.back_button = QAction(QIcon('./imgs/fanhui.png'),'Back',self)
        self.next_button = QAction(QIcon('./imgs/tiaozhuan.png'),'Forward',self)
        self.stop_button = QAction(QIcon('./imgs/close.png'),'Stop',self)
        self.reload_button = QAction(QIcon('./imgs/shuaxin.png'),'Reload',self)
        self.add_button = QAction(QIcon('./imgs/add.png'),'Addpage',self)

        self.set_default_openPage_button = QAction(QIcon('./imgs/liulanqi.png'),'SetDefault',self)



        self.main_toolbar.addAction(self.back_button)
        self.main_toolbar.addAction(self.next_button)
        self.main_toolbar.addAction(self.stop_button)
        self.main_toolbar.addAction(self.reload_button)
        self.main_toolbar.addAction(self.add_button)
        self.main_toolbar.addWidget(self.url_edit)
        self.main_toolbar.addAction(self.turn_button)

        self.main_toolbar.addAction(self.set_default_openPage_button)



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

    
    def defaultPage(self):
        text, ok=QInputDialog.getText(self, 'Text Input Dialog', '输入默认网址：')
        if ok :
            if text != "":
                # print(text)
                if repath.judge(text):
                    print(text)
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

    def NewPage(self,url='',label=''):
        browser = QWebEngineView()
        Url = 'https://cn.bing.com'
        browser.setUrl(QtCore.QUrl(Url))
        i = self.tabs.addTab(browser,label)
        self.tabs.setCurrentIndex(i)
        print(i)

        browser.loadFinished.connect(lambda :self.tabs.setTabText(i,browser.page().title()))

    def Closepage(self,i):
        # if self.tabs.count() < 2:
        #     return
        # self.tabs.removeTab(i)
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