# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : MainWindows.py
@Author : SuFIND
@Time : 2023/1/29 11:06
"""
from PyQt6.QtWidgets import QMainWindow

from ui.ui_MainWindows import Ui_MainWindow
from control.MenuOtherAboutDialog import MenuOtherAboutDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.handleActionAbout)

    def handleActionAbout(self):
        MenuOtherAboutDialog(self).exec()
