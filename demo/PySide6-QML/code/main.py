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
* 备注：
'''
import os, sys
import json
import traceback
import http.client
from PySide6.QtCore import Qt,QObject,Signal,Slot,Property,QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QLabel
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtQuick import QQuickWindow
from PySide6.QtQml import QQmlEngine, QQmlComponent


def send_error_log(message):
    try:
        url = "192.168.10.83:4444"
        endpoint = "/"
        data = json.dumps({"message": message})
        headers = {"Content-type": "application/json"}
        conn = http.client.HTTPConnection(url, timeout=0.05)
        conn.request("POST", endpoint, data, headers)
    except:
        pass


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


class Backend(QObject):
    '''
    后端控制程序
    '''
    # 信号：用于从Python向QML发送数据
    textChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self._text = "PySide6 APP"

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
        print("QML msg", msg)

    # 槽：供QML调用的方法
    @Slot(str)
    def qmlCallback(self, message):
        print("QML says:", message)



if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    send_error_log("App run Start")
    try:
        # 初始化QQuickWindow
        window = QQuickWindow()
        window.setTitle("PySide6 QQuickWindow 示例")
        window.resize(800, 600)

        # 创建QML引擎和组件
        engine = QQmlEngine()
        backend = Backend()
        engine.rootContext().setContextProperty("backend", backend)
        component = QQmlComponent(engine)
        component.loadUrl(QUrl.fromLocalFile("main.qml"))

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
                print("错误：无法创建QML组件")
                print(component.errorString())
                sys.exit(1)
        else:
            print("错误：QML组件加载失败")
            print(component.errorString())
            sys.exit(1)
    except:
        ret = traceback.format_exc()
        send_error_log(ret)
        mWin = Starter(ret)
        mWin.show()
    sys.exit(qapp.exec())