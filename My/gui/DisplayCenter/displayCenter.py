"""
    页面在电脑屏幕居中显示
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

class MainWin01(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # 设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口尺寸
        self.resize(500, 300)

        self.center()

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        # 左上角x坐标
        leftx = (screen.width()-size.width()) / 2
        # 左上角y坐标
        lefty = (screen.height()-size.height()) / 2
        # self.move(leftx, lefty)
        self.move(int(leftx), int(lefty))

if __name__ == '__main__':
    # 创建程序
    app = QApplication(sys.argv)
    # 创建窗口
    w = MainWin01()
    # 展示窗口
    w.show()
    # 进入程序主循环
    sys.exit(app.exec_())