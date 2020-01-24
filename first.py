# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\gurd\first.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import xlrd 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap


tags_name={'005B30DE':'اراک','005B4433':'motor khaneh','00A4E9AC':'solar panels',
'00A99ADD':'karghah door','0060920D':'anbar malzomat','00746592':'mashonalat edareh',
'007474E4':'gym','00747BBA':'mashinalat behind','00A9ABE0':'oil anbar',
'005B440D':'‍gas station','005B3C1A':'corner tower','00747435':'center tower','00607A0B':'karghah mohavateh'}


   


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(30, 20, 451, 401))
        self.label_img.setObjectName("label_img")         
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 30, 511, 511))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(630, 260, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.loc_Button = QtWidgets.QToolButton(self.centralwidget)
        self.loc_Button.setGeometry(QtCore.QRect(770, 260, 25, 19))
        self.loc_Button.setObjectName("loc_Button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.printer)
        self.loc_Button.clicked.connect(self.select_file)

        
        self.label_img.setPixmap(QPixmap("Tulips.jpg"))
        self.label_img.setGeometry(0,0,800,800)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "run"))
        self.loc_Button.setText(_translate("MainWindow", "..."))
        self.label_img.setText(_translate("MainWindow", "TextLabel"))

    def printer(self):  
        
        line_count=0
        l=list()
        d=dict()
        l2=list()


        address=self.lineEdit.text()
        #print(self.lineEdit.text())
    
        #address=input('Enter file path :')

        excel_reader=xlrd.open_workbook(address) 
        sheet = excel_reader.sheet_by_index(0) 
        sheet.cell_value(0, 0) 


        for i in range(0,sheet.nrows):
            
            row=sheet.row_values(i)
            
            if line_count > 1:

                l.append((row[2],row[3][11:]) )
                
                
            line_count +=1
            

        i=len(l)-1

        while i >= 0 :
            
            x=l[i][0]
            k=0
            for j in reversed(range(0,len(l))):

                if l[j][0] == x :

                    l2.append(l[j][1])
                    l.pop(j)
                    k+=1

            
            i=len(l)-1  
            d[x]=l2[(len(l2)-k):]  


        #print(self.lineEdit.text())

        for i in d:
            pass
            self.textBrowser.append(tags_name[i])
            self.textBrowser.append(str(d[i]))
            self.textBrowser.append("\n*****************************")

    def select_file(self):
        self.lineEdit.setText(QFileDialog.getOpenFileName()[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
