import sys
import time
from datetime import datetime

import winsound
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import QTimer
import psutil


class BatteryMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_battery_info)
        self.timer.start(1000)  # 更新频率为1秒

        self.frequency = 2000  # 蜂鸣的频率（Hz）
        self.duration = 11500  # 蜂鸣的持续时间（毫秒）



    def initUI(self):
        self.setWindowTitle('Battery Monitor')
        self.layout = QVBoxLayout()
        self.percentage_label = QLabel('')
        self.status_label = QLabel('')
        self.open_label = QLabel('')
        self.already_open_label = QLabel('')
        self.layout.addWidget(self.percentage_label)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.open_label)
        self.layout.addWidget(self.already_open_label)
        self.setLayout(self.layout)



    def update_battery_info(self):
        battery = psutil.sensors_battery()

        now_time = datetime.now()
        now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")  # 字符串类型
        now_time = datetime.strptime(now_time, r"%Y-%m-%d %H:%M:%S")  # 将字符串类型转为datetime.datetime类型

        last_time = psutil.boot_time()
        last_time = datetime.utcfromtimestamp(last_time)    # 将float类型转为datetime.datetime类型

        end_time = now_time - last_time
        end_time = str(end_time)
        self.already_open_label.setText('系统已启动时间: ' + end_time)


        self.open_label.setText(time.strftime('系统启动时间: '+'%Y-%m-%d %H:%M:%S', time.localtime(psutil.boot_time())))



        if battery:
            self.percentage_label.setText(f'{battery.percent}%')

            # 当电量少于30%时，发出蜂鸣声
            int_battery = int(battery.percent)
            if int_battery <= 30:
                winsound.Beep(self.frequency, self.duration)

            # 显示当前充电状态
            if battery.power_plugged:
                self.status_label.setText('Plugged')
            else:
                self.status_label.setText('Unplugged')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BatteryMonitor()
    ex.show()
    sys.exit(app.exec_())
