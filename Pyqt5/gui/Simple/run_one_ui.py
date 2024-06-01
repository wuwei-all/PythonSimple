"""
    调用界面.ui文件
"""
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class run_one_ui:
    def __init__(self):
        # 动态加载UI文件
        self.ui = uic.loadUi('one.ui')

if __name__ == "__main__":
    app = QApplication([])
    win = run_one_ui()
    win.ui.show()
    app.exec_()