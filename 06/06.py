"""
    列表的循环
"""

# 使用while循环列表
def list_while_func():
    my_list = ["zhangsan","lisi","wangwu"]
    index = 0
    while index < len(my_list):
        element = my_list[index]

        print(f"列表的元素为：{element}")
        index += 1

list_while_func()

print("******************")

# 使用for循环循环列表
def list_for_func():
    my_list = ["zhangsan","lisi","wangwu"]
    for element in my_list:
        print(f"列表的元素为：{element}")

list_for_func()