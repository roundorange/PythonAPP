#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###----------1、文件说明----------###
'''
* 说明：手机APP中，启动PySide6-QML代码的启动代码。出错时会发送错误信息
* 时间：2025-04-25 21:09:43
* 文件：
* 作者：Smile
* 版本：
    - 1.0 启动PySide6代码的启动代码，出错时会发送报错信息，并启动另一个界面，显示报错信息
    - 1.1 添加loguru库，使用了post日志流
        - 1.1.1 使用log.info函数打印信息，qDebug不能打印行号、函数名
* 备注：
'''
import os, sys
import json
import time
import traceback
import platform
import http.client
import PySide6
from PySide6.QtCore import Qt,QObject,Signal,Slot,Property,QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QLabel
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtQuick import QQuickWindow
from PySide6.QtQml import QQmlEngine, QQmlComponent
from PySide6.QtCore import qInstallMessageHandler, QtMsgType
from PySide6.QtCore import qDebug,qInfo,qWarning,qCritical,qFatal
from loguru import logger as log
from pprint import pprint

APPNAME = "PySide6"
APPVERSION = "1.0"

def post_to_remote(message):
    """将日志通过POST发送到远程服务器"""
    log_entry = {
        "file": message.record["file"].name,
        "filepath": message.record["file"].path,
        "function": message.record["function"],
        "level": message.record["level"].name,
        "line": message.record["line"],
        "module": message.record["module"],
        "message": message.record["message"],
        "process": message.record["process"].name + "(" + str(message.record["process"].id) + ")",
        "thread": message.record["thread"].name + "(" + str(message.record["thread"].id) + ")",
        "timestamp": message.record["time"].isoformat(),
        "extra": message.record["extra"],
    }
    try:
        url = "192.168.10.83:54444"
        # url = "192.168.10.20:54444"
        endpoint = "/"
        headers = {"Content-type": "application/json"}
        conn = http.client.HTTPConnection(url, timeout=0.05)
        conn.request("POST", endpoint, json.dumps(log_entry, ensure_ascii=False).encode("utf-8"), headers)
    except Exception as e:
        # 如果远程日志失败，可以回退到本地日志
        qWarning(f"Failed to send log to remote: {str(e)}")

# 添加post日志
log.add(post_to_remote, level="DEBUG")
# 添加日志文件
if platform.system() == "Windows":
    log.add(f"{APPNAME}-{APPVERSION}-{time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())}.log", backtrace=True, diagnose=True, level="DEBUG")
else:
    log.add(f"/storage/emulated/0/Download/{APPNAME}-{APPVERSION}-{time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())}.log", backtrace=True, diagnose=True, level="DEBUG")

# 自定义日志处理函数
def qt_message_handler(mode, context, message):
    if mode == QtMsgType.QtInfoMsg:
        mode = "Info"
        log.info(f"{context.file}:{context.line}-->{mode}: {message}")
    elif mode == QtMsgType.QtWarningMsg:
        mode = "Warning"
        log.warning(f"{context.file}:{context.line}-->{mode}: {message}")
    elif mode == QtMsgType.QtCriticalMsg:
        mode = "Critical"
        log.critical(f"{context.file}:{context.line}-->{mode}: {message}")
    elif mode == QtMsgType.QtFatalMsg:
        mode = "Fatal"
        log.error(f"{context.file}:{context.line}-->{mode}: {message}")
    else:
        mode = "Debug"
        log.debug(f"{context.file}:{context.line}-->{mode}: {message}")
# 安装日志处理函数
qInstallMessageHandler(qt_message_handler)

class Starter(QMainWindow):
    def __init__(self, errormsg):
        super(Starter, self).__init__()
        self.setWindowTitle("PySide6应用启动器")
        self.resize(550, 800)
        self.initGUI(errormsg)

    def initGUI(self, showtxt):
        self.widget = QWidget(self)
        layout = QVBoxLayout(self.widget)
        # 第一行
        self.title = QLabel("PySide6应用启动器")
        self.title.setStyleSheet("font: 24pt")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedHeight(50)
        layout.addWidget(self.title)
        # 第二行
        self.textedit = QTextEdit(self.widget)
        self.textedit.setText(showtxt)
        layout.addWidget(self.textedit)
        # 设置主要显示区
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    log.info(f"PySide6 Version {PySide6.__version__}")
    try:
        # 导入测试库
        from FluentUI import FluentUI
        from appsrc import Backend

        # 初始化QQuickWindow
        window = QQuickWindow()
        window.setTitle("PySide6 QQuickWindow 示例")
        window.resize(800, 600)

        # 创建QML引擎和组件
        engine = QQmlEngine()
        FluentUI.registerTypes(engine)
        engine.addImportPath(os.path.join(os.path.dirname(__file__), "qml"))  # 添加 QML 模块搜索路径

        backend = Backend()
        engine.rootContext().setContextProperty("backend", backend)
        component = QQmlComponent(engine)
        component.loadUrl(QUrl.fromLocalFile("qml/App-QQuickWindow.qml")) # 简单单页面
        # component.loadUrl(QUrl.fromLocalFile("qml/App-Four.qml"))         # 四个页面切换

        if component.isReady():
            # 创建QML根对象
            qml_object = component.create()
            if qml_object:
                # 将QML对象设置为窗口内容
                qml_object.setParentItem(window.contentItem())
                # 自动调整窗口大小到根对象尺寸
                window.resize(qml_object.width(), qml_object.height())
                window.resize(350, 600)  # 临时使用
                window.show()
            else:
                log.error("错误：无法创建QML组件")
                log.error(component.errorString())
                sys.exit(1)
        else:
            log.error("错误：QML组件加载失败")
            log.error(component.errorString())
            sys.exit(1)
    except:
        ret = traceback.format_exc()
        log.error(ret)
        mWin = Starter(ret)
        mWin.show()
    sys.exit(qapp.exec())