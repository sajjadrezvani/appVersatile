# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_welcomeWin(object):
    def setupUi(self, welcomeWin):
        welcomeWin.setObjectName("welcomeWin")
        welcomeWin.resize(200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(welcomeWin.sizePolicy().hasHeightForWidth())
        welcomeWin.setSizePolicy(sizePolicy)
        welcomeWin.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(welcomeWin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(400, 1677721))
        self.label_2.setAcceptDrops(False)
        self.label_2.setStatusTip("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(255, 200, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/versatile (3).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalFrame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.verticalFrame)
        welcomeWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(welcomeWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        welcomeWin.setMenuBar(self.menubar)

        self.retranslateUi(welcomeWin)
        QtCore.QMetaObject.connectSlotsByName(welcomeWin)

    def retranslateUi(self, welcomeWin):
        _translate = QtCore.QCoreApplication.translate
        welcomeWin.setWindowTitle(_translate("welcomeWin", "MainWindow"))
        self.label_3.setText(_translate("welcomeWin", "welcome to Versatile app by Sajjad Rezvani.K for TNM\n"
" You can use this app for serveral purposes \n"
" Enjoy! "))
        self.label.setText(_translate("welcomeWin", "Enter your username:"))
        self.label_4.setText(_translate("welcomeWin", "Enter your password:"))
        self.pushButton.setText(_translate("welcomeWin", "Enter"))
import new_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcomeWin = QtWidgets.QMainWindow()
    ui = Ui_welcomeWin()
    ui.setupUi(welcomeWin)
    welcomeWin.show()
    sys.exit(app.exec_())