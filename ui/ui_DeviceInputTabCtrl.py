# Form implementation generated from reading ui file 'designer\DeviceInputTabWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DeviceInputTabCtrl(object):
    def setupUi(self, DeviceInputTabCtrl):
        DeviceInputTabCtrl.setObjectName("DeviceInputTabWidget")
        DeviceInputTabCtrl.resize(583, 379)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DeviceInputTabCtrl)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=DeviceInputTabCtrl)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MouseCheck = QtWidgets.QCheckBox(parent=self.frame)
        self.MouseCheck.setObjectName("MouseCheck")
        self.horizontalLayout_2.addWidget(self.MouseCheck)
        self.KeyboardCeck = QtWidgets.QCheckBox(parent=self.frame)
        self.KeyboardCeck.setObjectName("KeyboardCeck")
        self.horizontalLayout_2.addWidget(self.KeyboardCeck)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveButton = QtWidgets.QPushButton(parent=self.frame)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.ClearButton = QtWidgets.QPushButton(parent=self.frame)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout.addWidget(self.ClearButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)
        self.logBrowser = QtWidgets.QTextBrowser(parent=DeviceInputTabCtrl)
        self.logBrowser.setObjectName("logBrowser")
        self.verticalLayout.addWidget(self.logBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DeviceInputTabCtrl)
        QtCore.QMetaObject.connectSlotsByName(DeviceInputTabCtrl)

    def retranslateUi(self, DeviceInputTabCtrl):
        _translate = QtCore.QCoreApplication.translate
        DeviceInputTabCtrl.setWindowTitle(_translate("DeviceInputTabWidget", "Form"))
        self.MouseCheck.setText(_translate("DeviceInputTabWidget", "MouseEvent"))
        self.KeyboardCeck.setText(_translate("DeviceInputTabWidget", "KeyboardEvent"))
        self.SaveButton.setText(_translate("DeviceInputTabWidget", "Save"))
        self.ClearButton.setText(_translate("DeviceInputTabWidget", "Clear"))
        self.MouseCheck.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.KeyboardCeck.setCheckState(QtCore.Qt.CheckState.Checked)
