"""
    https://blog.csdn.net/La_vie_est_belle/article/details/82432252
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.checkbox1 = QCheckBox('checkbox1 use setChecked()', self)
        self.checkbox2 = QCheckBox('checkbox2 use setCheckState()', self)
        self.checkbox3 = QCheckBox('checkbox3 need setTristate(),setCheckState()', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):

        # 通过setChecked()方法传入True或者False可以将复选框设为选中或无选中状态；另外一种替代的方法是setCheckState()
        self.checkbox1.setChecked(True)

        # stateChanged信号会在复选框状态发生改变的时候发出。这里我们发现槽函数是带参数的，可以通过lambda表达式来将参数传入槽函数。若单纯使用self.on_state_change_func(self.checkbox2)则会报错
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))

        # setCheckState()，传入的参数可以是选中状态Qt.Checked, 无选中状态Qt.Unchecked和半选中状态Qt.PartiallyChecked
        self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        # 如果要让一个复选框拥有三种状态，则必须通过setTristate(True)方法来实现。在这里我们让第三个复选框拥有三种状态
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)  # 设置为半选中状态Qt.PartiallyChecked
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))

    # checkState()方法可以获取当前复选框的状态，返回值为int类型，0为无选中状态，1为半选中状态，2位选中状态
    def on_state_change_func(self, checkbox):
        print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())