import os
import pandas as pd
import time

# 文件路径
file_path = 'example.txt'
# Excel文件路径
excel_path = 'output.xlsx'

# 初始最后修改时间
last_modified = os.path.getmtime(file_path)


# 检测文件是否修改的函数
def check_file_modified():
    global last_modified
    current_modified = os.path.getmtime(file_path)
    if current_modified > last_modified:
        last_modified = current_modified
        return True
    return False


# 主循环
while True:
    if check_file_modified():
        # 文件被修改，输出最后修改时间到Excel
        modified_time = time.ctime(last_modified)
        original_data = pd.read_excel('output.xlsx')
        df = pd.DataFrame([modified_time], columns=['Last Modified'])

        # df = original_data.append(df)
        df = pd.concat([original_data,df])

        df.to_excel(excel_path, index=False)
        print(f"File modified at: {modified_time}")

    # 等待一段时间再次检查
    time.sleep(5)  # 每5秒检查一次