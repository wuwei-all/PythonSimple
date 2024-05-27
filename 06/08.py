"""
    字符串
"""
my_str = "zhangjie good"


# 通过下标索引取值，可以正向或反向

# index方法


# replace
print(f"原字符串：{my_str}")
new_my_str = my_str.replace("good","666")
print(f"替换后的字符串：{new_my_str}")

# split，注意元组切割后，类型转换为list
my_str = "zhangjie good"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型为：{type(my_str_list)}")

# strip,去除指定符号


# count

# len




