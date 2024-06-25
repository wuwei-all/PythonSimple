import os
import time
from io import StringIO

import pandas as pd
from openpyxl import load_workbook


def traverse_folder(folder_path):
    # 获取文件夹下的所有文件和文件夹

    files = os.listdir(folder_path)



    for file in files:
        # 拼接文件路径
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            # 如果是文件夹，则递归遍历
            traverse_folder(file_path)
        else:
            # 如果是文件，则打印文件路径
            print(file_path)
            print(type(file))
            print(file)

            modification_time = os.path.getmtime(file_path)
            readable_modification_time = time.ctime(modification_time)
            print("文件最后修改时间（以秒为单位）:", readable_modification_time)

            combined_str = file_path + "," + file
            print(combined_str)

            result = pd.read_csv(StringIO(combined_str), sep=",")
            print(type(result))

            # df = pd.DataFrame(result)
            # pd.concat(["text.xlsx",df])





    # df = pd.DataFrame(result)
    # df.to_excel("text.xlsx",index=False)

            # df.to_excel('data.xlsx', index=False)

traverse_folder('E:\\temp\\code')



