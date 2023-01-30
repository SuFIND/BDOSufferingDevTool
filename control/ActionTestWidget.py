# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : ActionTestWidget.py
@Author : FF
@Time : 2023/1/30 11:36
"""
from PyQt6 import QtWidgets, QtCore
from ui.ui_ActionTestWidget import Ui_ActionTestWidget


class ActionTestWidget(QtWidgets.QWidget):
    refresh_sig = QtCore.pyqtSignal(str)

    def __init__(self, parent, *args):
        super(ActionTestWidget, self).__init__(parent, *args)
        self.viewer = Ui_ActionTestWidget()
        self.viewer.setupUi(self)
