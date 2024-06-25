import os
import time


def traverse_dir(path):
    for root, dirs, files in os.walk(path):
        print("当前目录：", root)
        print("子目录列表：", dirs)
        for file in files:
            # 拼接文件路径
            file_path = os.path.join(root, file)

            modification_time = os.path.getmtime(file_path)
            readable_modification_time = time.ctime(modification_time)
            print("文件最后修改时间（以秒为单位）:", readable_modification_time)

            print("文件列表：", file)
            print(type(file))

        # modification_time = os.path.getmtime(files)
        #
        # # 打印文件最后修改时间（以秒为单位）
        # print("文件最后修改时间（以秒为单位）:", modification_time)

dir_path = "E:\\temp"
print('待遍历的目录为：', dir_path)
print('遍历结果为：')
traverse_dir(dir_path)