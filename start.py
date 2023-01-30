# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : start.py
@Author : FF
@Time : 2023/1/29 10:43
"""
import sys

from PyQt6.QtWidgets import QApplication

from control.MainWindows import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
