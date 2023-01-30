# -*- coding: utf-8 -*-
"""
@Project : BDOSufferingDevTool
@File : log_utils.py
@Author : FF
@Time : 2023/1/29 10:51
"""
import datetime

from PyQt6 import QtGui
from PyQt6.QtCore import Qt

textMap = {
    Qt.Key.Key_Shift: "shift",
    Qt.Key.Key_Alt: "alt",
    Qt.Key.Key_Control: "ctrl",
    Qt.Key.Key_Enter: "enter",
    Qt.Key.Key_Return: "return",
    Qt.Key.Key_Space: "space",
}


def formatKeyBoardLogs(ev: [QtGui.QKeyEvent], action: str, show_detail: bool = False) -> [str, None]:
    """
    格式化键盘事件
    :param ev: 事件
    :param action: 动作 press or release
    :param show_detail: 是否展示详细信息
    :return:
    """
    res = None
    if isinstance(ev, QtGui.QKeyEvent):
        key_text = textMap.get(ev.key(), ev.text())
        res = f"{action}\t‘{key_text}’"
        res += "" if not show_detail else f"\tvk_code={ev.nativeVirtualKey()} scan code={ev.nativeScanCode()}"
    return res


def stopLog(suffix=""):
    time_info = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}]'
    msg = "脚本停止运行" + suffix
    return f"{time_info} - {msg}\n"


def startLog(suffix=""):
    time_info = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}]'
    msg = "脚本开始运行" + suffix
    return f"{time_info} - {msg}\n"


def normalLog(msg):
    time_info = f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}]'
    msg = f"{msg}"
    return f"{time_info} - {msg}\n"