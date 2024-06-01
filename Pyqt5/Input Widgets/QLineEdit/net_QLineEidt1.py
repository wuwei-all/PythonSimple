"""
    验证器
    https://www.cnblogs.com/chenhaiming/p/9929252.html
"""
#导入，Qapplication，单行文本框，窗口，表单布局
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
#导入文本校验器：整数校验器与浮点数校验器,其他自定义校验器
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator

from PyQt5.QtCore import QRegExp
import sys

class lineEditDemo(QWidget):
    def __init__(self,parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle('QLineEdit例子')

        #实例化表单布局
        flo=QFormLayout()

        #创建三个文本框
        pIntLineEdit=QLineEdit()
        pDoubleLineEdit=QLineEdit()
        pValidatorLineEdit=QLineEdit()

        #表单布局添加名称及控件
        flo.addRow('整型',pIntLineEdit)
        flo.addRow('浮点型',pDoubleLineEdit)
        flo.addRow('字母和数字',pValidatorLineEdit)

        #设置文本框的默认浮现文本
        pIntLineEdit.setPlaceholderText('整型，1-99')
        pDoubleLineEdit.setPlaceholderText('浮点型，-360到360，精度2位小数')
        pValidatorLineEdit.setPlaceholderText('字母和数字')

        #整型 范围 【1-99】
        #实例化整型验证器，并设置范围为1-99
        pIntvalidator=QIntValidator(self)
        pIntvalidator.setRange(1,99)

        #浮点型 范围 【-360,360】，精度小数点后两位
        #实例化浮点验证器，设置范围-360到360
        pDoubleValidator=QDoubleValidator()
        pDoubleValidator.setRange(-360,360)

        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度小数点后两位
        pDoubleValidator.setDecimals(2)

        #字母和数字
        #设置文本允许出现的字符内容
        reg=QRegExp('[a-zA-Z0-9]+$')
        #自定义文本验证器
        pValidator=QRegExpValidator(self)
        #设置属性
        pValidator.setRegExp(reg)

        #设置验证器
        pIntLineEdit.setValidator(pIntvalidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=lineEditDemo()
    win.setGeometry(300,300,500,20)
    win.show()
    sys.exit(app.exec_())