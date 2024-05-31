"""
    https://blog.csdn.net/weixin_50064049/article/details/134897758
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QTimer, QDateTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 开启编辑器
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.counter = 1
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_text)
        # 每秒刷新一次
        self.timer.start(1000)
        # 展示页面
        self.show()

    def refresh_text(self):
        current_time = QDateTime.currentDateTime().toString("hh:mm:ss")
        # 更新当前页面信息
        text = f"{current_time}：当前数字为 {self.counter}"
        self.text_edit.setText(text)
        self.counter += 1
        # 到达 100 时停止定时器
        if self.counter > 100:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
