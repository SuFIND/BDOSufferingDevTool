# -*- coding: utf-8 -*-
import datetime
import time
import traceback

from PyQt6 import QtWidgets, QtCore
from ui.ui_ActionTestWidget import Ui_ActionTestWidget


class ActionTestWidget(QtWidgets.QWidget):
    refresh_sig = QtCore.pyqtSignal(str)

    def __init__(self, parent, *args):
        super(ActionTestWidget, self).__init__(parent, *args)
        self.viewer = Ui_ActionTestWidget()
        self.viewer.setupUi(self)

        # sig
        self.viewer.PlayButton.clicked.connect(self.PlayActions)
        self.refresh_sig.connect(self.RefreshActionLog)

        # data
        self.log = ""

    def AddLog(self, msg):
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log += f"[{time_str}] - {msg}\n"
        self.refresh_sig.emit("")

    def RefreshActionLog(self, sig):
        self.viewer.textBrowser.setText(self.log)

    def PlayActions(self):
        sec = 0
        if self.viewer.waitBeforPlayCheckBox.checkState() == QtCore.Qt.CheckState.Checked:
            try:
                sec = float(self.viewer.WaitSecLineEdit.text())
            except Exception:
                sec = 3
        try:
            self.AddLog(f"hello {sec}")
        except Exception as e:
            err = traceback.format_exc()
            self.AddLog(err)
