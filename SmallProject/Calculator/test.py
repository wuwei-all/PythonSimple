from datetime import datetime

import psutil

now_time = datetime.now()
now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
now_time = datetime.strptime(now_time, r"%Y-%m-%d %H:%M:%S")
print("当前时间", now_time)
print(type(now_time))
end_time = '2020/10/15 9:45:32'
end_time = datetime.strptime(end_time, r"%Y/%m/%d %H:%M:%S")
print(end_time)
print(type(end_time))
diff = now_time - end_time
print("时间差", diff)
print("两时间相差多少秒", diff.total_seconds())

print(u"系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
