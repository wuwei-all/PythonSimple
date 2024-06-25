import os
#批量替换文件名
def change_file(target_path):
    for file_name in os.listdir(target_path):
        file_path = os.path.join(target_path,file_name)
        #判断路径是否为文件
        if os.path.isdir(file_path):
            change_file(file_path)
        else:
            new_file_name = file_name.replace(old_str, new_str)
            #法一：比对新旧文件名，不一致则重命名文件
            if new_file_name != file_name:
                os.rename(file_path, os.path.join(target_path, new_file_name))
                print('旧文件'+file_name+'已重命名为：'+new_file_name)
#批量替换文件夹名
def change_folder(target_path):
    for file_name in os.listdir(target_path):
        file_path = os.path.join(target_path,file_name)
        if os.path.isdir(file_path):
            new_folder_name = file_path.replace(old_str,new_str)
            #法二：直接重命名，命名失败则抛出异常
            try:
                os.rename(file_path,new_folder_name)
                print(f'{file_path} 已重命名为： {new_folder_name}')
                change_folder(new_folder_name)
            except Exception as e:
                print('文件夹'+file_path+'重命名失败。报错：'+ e)
# 根目录
target_path = r"E:\\temp\\24"
#待替换字符串
old_str = ","
#新字符串
new_str = "-"
change_file(target_path)
change_folder(target_path)