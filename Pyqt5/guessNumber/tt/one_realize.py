import sys

from PyQt5.QtWidgets import QApplication, QStackedLayout, QMainWindow, QMessageBox, QWidget
import one

import random



class MainWidget(QWidget, one.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(1400, 1200)
        self.answer = random.randint(0, 100)
        self.lineEdit.setPlaceholderText('请在这里数字')
        test = self.lineEdit.text()
        self.lineEdit_2.setText(test)
        # self.lineEdit.toPlainText()
        # self.setWindowFlags(self.Window)  # 设置窗口最大化最小化，不能实现

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()
    sys.exit(app.exec_())