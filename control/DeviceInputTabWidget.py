# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : DeviceInputTabWidget.py
@Author : SuFIND
@Time : 2023/1/29 11:05
"""
import os
import datetime

from PyQt6 import QtWidgets, QtGui, QtCore
from ui.ui_DeviceInputTabCtrl import Ui_DeviceInputTabCtrl
from utils.log_utils import formatKeyBoardLogs


class DeviceInputTabWidget(QtWidgets.QWidget):
    refresh_sig = QtCore.pyqtSignal(str)

    def __init__(self, parent, *args):
        super(DeviceInputTabWidget, self).__init__(parent, *args)
        self.viewer = Ui_DeviceInputTabCtrl()
        self.viewer.setupUi(self)

        # 缓存变量值
        self.logLines = []

        # 绑定信号事件
        self.refresh_sig.connect(self.refresh)
        self.viewer.MouseCheck.stateChanged.connect(self.trackMouse)
        self.viewer.SaveButton.clicked.connect(self.saveLogBrowse)
        self.viewer.ClearButton.clicked.connect(self.clearLogBrowse)

    def addLog(self, msg: str, acc_time: str = None) -> None:
        """
        向日志展示控件添加日志
        :param msg:
        :param acc_time:
        :return:
        """
        # 是否指定了日志事件
        if acc_time is not None:
            time_str = acc_time
        else:
            time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        format_msg = f"[{time_str}] - {msg}"
        self.logLines.append(format_msg)
        self.refresh_sig.emit("logBrowser")

    def refresh(self, sig: str) -> None:
        """
        刷新控件
        :param sig:
        :return:
        """
        if sig.find("logBrowser") != -1:
            self.refreshLogBrowse()

    def refreshLogBrowse(self) -> None:
        """
        刷新日志浏览widget
        :return:
        """
        txt = ""
        for line in self.logLines:
            txt += f"{line}\n"
        self.viewer.logBrowser.setPlainText(txt)
        self.viewer.logBrowser.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def clearLogBrowse(self) -> None:
        """
        刷新日志浏览widget
        :return:
        """
        txt = ""
        self.logLines = []
        self.viewer.logBrowser.setPlainText(txt)

    def saveLogBrowse(self) -> None:
        """
        保存日志
        :return:
        """
        plain_txt = self.viewer.logBrowser.toPlainText()
        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                          caption="保存日志文件",
                                                                          directory=os.getcwd(),  # 起始路径
                                                                          initialFilter="*.log")
        if fileName_choose == "":
            # 取消选择
            return

        with open(fileName_choose, 'w', encoding="utf-8") as fp:
            fp.write(plain_txt)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if self.viewer.KeyboardCeck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        if a0.isAutoRepeat():
            return
        key_msg = formatKeyBoardLogs(a0, 'press', show_detail=True)
        self.addLog(key_msg)

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if self.viewer.KeyboardCeck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        if a0.isAutoRepeat():
            return
        key_msg = formatKeyBoardLogs(a0, 'release', show_detail=True)
        self.addLog(key_msg)

    def trackMouse(self):
        flag = True if self.viewer.MouseCheck.checkState() == QtCore.Qt.CheckState.Checked else False
        self.setMouseTracking(flag)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.viewer.MouseCheck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        pos = a0.pos()
        msg = f"mouse move to\t({pos.x()}, {pos.y()})}}"
        self.addLog(msg)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.viewer.MouseCheck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        pos = a0.pos()
        msg = f"mouse press at\t({pos.x()}, {pos.y()})}}"
        self.addLog(msg)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.viewer.MouseCheck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        pos = a0.pos()
        msg = f"mouse release at\t({pos.x()}, {pos.y()})}}"
        self.addLog(msg)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.viewer.MouseCheck.checkState() != QtCore.Qt.CheckState.Checked:
            return
        pos = a0.pos()
        msg = f"mouse double click at\t({pos.x()}, {pos.y()})}}"
        self.addLog(msg)
