"""
    没有选中checkable属性，也可以触发clicked事件

    没有选中checkable属性，就不可以触发toggled事件！触发QPushButton的toggled事件，就要选中checkable属性！

    选中checkable属性，除了触发toggled事件，还可以有明显的颜色变化，按一下从灰色变淡蓝色，再按一下才从淡蓝色渐变回灰色；无论能不能触发事件，只要选中了checkable属性，就一定有这样的颜色变化！
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QRadioButton, QCheckBox

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 以下全部是setCheckable(True)
        self.test_button1 = QPushButton('setCheckable(True)', self)
        self.test_button1.setCheckable(True)
        self.test_button1.clicked.connect(lambda:self.on_clicked(self.test_button1))
        self.test_button1.toggled.connect(lambda:self.on_toggled(self.test_button1))

        self.test_button2 = QPushButton('setCheckable(True) AND setChecked(True)', self)
        self.test_button2.setCheckable(True)
        self.test_button2.setChecked(True)
        self.test_button2.clicked.connect(lambda: self.on_clicked(self.test_button2))
        self.test_button2.toggled.connect(lambda: self.on_toggled(self.test_button2))

        self.test_button3 = QPushButton('setCheckable(True) AND setChecked(False)', self)
        self.test_button3.setCheckable(True)
        self.test_button3.setChecked(False)
        self.test_button3.clicked.connect(lambda: self.on_clicked(self.test_button3))
        self.test_button3.toggled.connect(lambda: self.on_toggled(self.test_button3))


        # 以下全部是setCheckable(False)
        self.test_button5 = QPushButton('setCheckable(False)', self)
        self.test_button5.setCheckable(False)
        self.test_button5.clicked.connect(lambda: self.on_clicked(self.test_button5))
        self.test_button5.toggled.connect(lambda: self.on_toggled(self.test_button5))

        self.test_button6 = QPushButton('setCheckable(False) AND setChecked(False)', self)
        self.test_button6.setCheckable(False)
        self.test_button6.setChecked(False)
        self.test_button6.clicked.connect(lambda: self.on_clicked(self.test_button6))
        self.test_button6.toggled.connect(lambda: self.on_toggled(self.test_button6))

        self.test_button7 = QPushButton('setCheckable(False) AND setChecked(True)', self)
        self.test_button7.setCheckable(False)
        self.test_button7.setChecked(True)          # setChecked(True)不会展示出来，因为setCheckable(false)将禁止按钮被选中，即使使用setChecked(true)也无法改变按钮的状态
        self.test_button7.clicked.connect(lambda: self.on_clicked(self.test_button7))
        self.test_button7.toggled.connect(lambda: self.on_toggled(self.test_button7))

        # 实例化一个水平布局管理器
        self.h_layout = QHBoxLayout()

        self.h_layout.addWidget(self.test_button1)
        self.h_layout.addWidget(self.test_button2)
        self.h_layout.addWidget(self.test_button3)

        self.h_layout.addWidget(self.test_button5)
        self.h_layout.addWidget(self.test_button6)
        self.h_layout.addWidget(self.test_button7)

        # 将self.h_layout设为整个窗口的最终布局方式。
        self.setLayout(self.h_layout)

    def on_clicked(self, checkbox):
        print('{} was clicked on_clicked'.format(checkbox.text()))

    def on_toggled(self, checkbox):
        print('{} was clicked on_toggled'.format(checkbox.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())