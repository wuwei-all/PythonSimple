"""
    输入掩码
    https://www.cnblogs.com/chenhaiming/p/9929252.html
"""
from PyQt5.QtWidgets import QApplication,QLineEdit,QFormLayout,QWidget
import sys

class lineEditDemo(QWidget):
    def __init__(self,parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle('QlineEdit的掩码输入例子')

        #实例化表单布局
        flo=QFormLayout()
        #创建4个文本框
        pIPlineEdit=QLineEdit()
        pMAXlineEdit=QLineEdit()
        pDatelineEdit=QLineEdit()
        pLiceseLineEdit=QLineEdit()

        #setInputMask():设置掩码

        #ip地址掩码
        pIPlineEdit.setInputMask('000.000.000.000;_')
        #Mac地址掩码
        pMAXlineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        #日期掩码
        pDatelineEdit.setInputMask('0000-00-00')
        #许可证掩码
        pLiceseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')


        #添加名称与控件到表单布局中
        flo.addRow('数字掩码',pIPlineEdit)
        flo.addRow('Mac掩码',pMAXlineEdit)
        flo.addRow('日期掩码',pDatelineEdit)
        flo.addRow('许可证掩码',pLiceseLineEdit)

        #设置窗口的布局
        self.setLayout(flo)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=lineEditDemo()
    win.show()
    sys.exit(app.exec_())