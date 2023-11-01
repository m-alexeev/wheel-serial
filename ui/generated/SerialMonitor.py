# Form implementation generated from reading ui file '.\ui\designer\Serial Monitor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(774, 545)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Frame)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 493))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serialText = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.serialText.setBaseSize(QtCore.QSize(720, 480))
        self.serialText.setText("")
        self.serialText.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.serialText.setObjectName("serialText")
        self.horizontalLayout.addWidget(self.serialText)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timestampCheck = QtWidgets.QCheckBox(parent=Frame)
        self.timestampCheck.setObjectName("timestampCheck")
        self.horizontalLayout_2.addWidget(self.timestampCheck)
        self.scrollBottomCheck = QtWidgets.QCheckBox(parent=Frame)
        self.scrollBottomCheck.setObjectName("scrollBottomCheck")
        self.horizontalLayout_2.addWidget(self.scrollBottomCheck)
        self.closeMonitor = QtWidgets.QPushButton(parent=Frame)
        self.closeMonitor.setObjectName("closeMonitor")
        self.horizontalLayout_2.addWidget(self.closeMonitor)
        self.clearMonitor = QtWidgets.QPushButton(parent=Frame)
        self.clearMonitor.setObjectName("clearMonitor")
        self.horizontalLayout_2.addWidget(self.clearMonitor)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.timestampCheck.setText(_translate("Frame", "Enable Timestamp"))
        self.scrollBottomCheck.setText(_translate("Frame", "Scroll to Bottom"))
        self.closeMonitor.setText(_translate("Frame", "Close"))
        self.clearMonitor.setText(_translate("Frame", "Clear Output"))
