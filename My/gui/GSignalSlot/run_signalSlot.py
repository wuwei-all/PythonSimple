"""
    调用界面.py文件
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from signalSolt import Ui_Form

# 继承 QWidget类和 Ui_Form界面类
class run_signalSlot(QWidget, Ui_Form):
    # 初始化
    def __init__(self):
        # 调用父类（QWidget类和 Ui_Form界面类）的初始化函数
        # super().__init__()是Python3.0的写法
        super().__init__()    # super(run_one_py,self).__init__()两者等价,Python2.0写法
        # 继承 Ui_Form界面类的setupUi函数
        self.setupUi(self)

if __name__ == '__main__':
    # 在 QApplication 方法中使用，创建应用程序对象
    app = QApplication([])
    # 实例化 run_one_py 类，创建主窗口
    win = run_signalSlot()
    # 在桌面显示控件 win
    win.show()
    # 结束进程，退出程序
    sys.exit(app.exec_())