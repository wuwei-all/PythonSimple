import os
import time
from io import StringIO
import pandas as pd


# Excel文件路径
excel_path = 'ex.xlsx'

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
            modification_time = os.path.getmtime(file_path)
            readable_modification_time = time.ctime(modification_time)
            print("文件最后修改时间（以秒为单位）:", readable_modification_time)

            # 获取文件的大小
            file_size = os.path.getsize(file_path)
            # file_size = float(file_size/1000)
            file_size = str(file_size)
            # file_size = file_size+"MB"

            combined_str = file_path + "," + file + "," + readable_modification_time + "," + file_size
            print(combined_str)

            result = pd.read_csv(StringIO(combined_str), sep=",")
            print(type(result))
            print(result)

            original_data = pd.read_excel('ex.xlsx')
            df = pd.DataFrame([result.columns], columns=['file_path','file_name','last_time','file_size'])

            # df = original_data.append(df)
            df = pd.concat([original_data, df])

            df.to_excel(excel_path, index=False)
            print(f"File modified at: {result}")


traverse_folder('E:\\temp\\24')



