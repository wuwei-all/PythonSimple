from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import sys

class MainPanel(QWidget):
    def __init__(self):
        super(MainPanel, self).__init__()
        self.resize(400, 400)
        mainPanel_layout = QHBoxLayout()

        button_layout = QVBoxLayout()
        select_Panel1_button = QPushButton("标准计算器")
        select_Panel2_button = QPushButton("程序员计算器")
        select_Panel3_button = QPushButton("panel3")
        button_layout.addWidget(select_Panel1_button)
        button_layout.addWidget(select_Panel2_button)
        button_layout.addWidget(select_Panel3_button)

        one = onePanel()
        two = twoPanel()
        three = threePanel()

        qls = QStackedLayout()
        qls.addWidget(one)
        qls.addWidget(two)
        qls.addWidget(three)

        mainPanel_layout.addLayout(button_layout)
        mainPanel_layout.addLayout(qls)

        select_Panel1_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel1_button, qls))
        select_Panel2_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel2_button, qls))
        select_Panel3_button.clicked.connect(lambda: self.buttonIsClicked(select_Panel3_button, qls))

        self.setLayout(mainPanel_layout)

    def buttonIsClicked(self, button, qls):
        dic = {
            "标准计算器": 0,
            "程序员计算器": 1,
            "panel3": 2
        }
        index = dic[button.text()]
        qls.setCurrentIndex(index)


class onePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计算器")
        self.setWindowIcon(QIcon("./img/icon.png"))
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.result_display = QLineEdit()
        # 禁止直接输入
        # self.result_display.setReadOnly(True)

        # 设置最多显示的数字长度
        # self.result_display.setMaxLength(15)
        self.layout.addWidget(self.result_display)
        self.buttons = [
            ['AC', 'DEL', '', ''],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        self.grid_layout = QGridLayout()  # 对按钮使用网格布局
        self.layout.addLayout(self.grid_layout)
        self.create_buttons()

    def create_buttons(self):
        """
        生成按钮并绑定槽函数，然后放置在网格布局中
        """
        row = 0
        for button_row in self.buttons:
            col = 0
            for button_text in button_row:
                button = QPushButton(button_text)
                button.clicked.connect(self.button_clicked)
                self.grid_layout.addWidget(button, row, col)
                col += 1
            row += 1

    def button_clicked(self):
        button = self.sender()  # self.sender()获取发出信号的对象
        text = button.text()

        if text == 'AC':
            self.result_display.setText(self.result_display.clear())
        elif text == 'DEL':
            DLastCharacter = self.result_display.text()
            DLastCharacter = DLastCharacter[:-1]
            self.result_display.setText(DLastCharacter)

        elif text == '=':
            expression = self.result_display.text()
            try:
                result = eval(expression)  # eval:去除表达式的引号，这里的作用是变成表达式进行计算
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        else:
            #  如果不是按下=号，把输入数字追加到文本框
            self.result_display.setText(self.result_display.text() + text)


class twoPanel(QWidget):
    def __init__(self):
        super(twoPanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#66ffcc;}''')

        twoPanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面2")
        twoPanel_layout.addWidget(qlabel)

        self.setLayout(twoPanel_layout)

class threePanel(QWidget):
    def __init__(self):
        super(threePanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#ee0000;}''')

        threePanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面3")
        threePanel_layout.addWidget(qlabel)

        self.setLayout(threePanel_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainPanel()
    main.show()
    sys.exit(app.exec_())