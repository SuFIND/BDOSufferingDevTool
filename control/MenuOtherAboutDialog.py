# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : MenuOtherAboutDialog.py
@Author : FF
@Time : 2023/1/30 14:23
"""
from PyQt6.QtGui import QMouseEvent, QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QDialog
from ui.ui_MenuOtherAboutDialog import Ui_Dialog


class MenuOtherAboutDialog(QDialog):
    def __init__(self, parent, *args):
        super(MenuOtherAboutDialog, self).__init__(parent, *args)
        self.viewer = Ui_Dialog()
        self.viewer.setupUi(self)

        self.viewer.License.mouseReleaseEvent = self.handleLicense
        self.viewer.github.mouseReleaseEvent = self.handleToGithub

    def handleLicense(self, a0: QMouseEvent) -> None:
        QDesktopServices.openUrl(QUrl("https://www.gnu.org/licenses/gpl-3.0.en.html"))

    def handleToGithub(self, a0: QMouseEvent) -> None:
        QDesktopServices.openUrl(QUrl("https://github.com/SuFIND/BDOSufferingDevTool"))
