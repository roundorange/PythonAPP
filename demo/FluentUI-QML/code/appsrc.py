#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###----------1、文件说明----------###
'''
* 说明：python程序模板
* 时间：
* 文件：
* 作者：Smile
* 版本：0.1
* 备注：
'''
###----------2、库导入----------###
import os, sys
from PySide6.QtCore import QObject,Signal,Slot,Property
from loguru import logger as log
###----------3、参数配置----------###

###----------4、主体程序----------###
class Backend(QObject):
    '''
    后端控制程序
    '''
    # 信号：用于从Python向QML发送数据
    textChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self._text = "PySide6 QML APP"

    # <---------- text属性管理 ---------->
    def get_text(self):
        return self._text
    def set_text(self, value):
        self._text = value
        self.textChanged.emit(value)  # 属性变化时发射信号
    text = Property(str, get_text, set_text, notify=textChanged)

    # 槽：供QML调用的方法
    @Slot(str)
    def debug(self, msg):
        log.debug(f"QML msg: {msg}")

    # 槽：供QML调用的方法
    @Slot(str)
    def qmlCallback(self, message):
        log.debug(f"QML says: {message}")
