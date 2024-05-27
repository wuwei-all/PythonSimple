"""
    正向
"""
# 对list进行切片，从1开始，4结束，步长1
my_list = [0,1,2,3,4,5,6]
result = my_list[1:4]   # 步长默认为1，可以省略不写
print(f"{result}")

# 对tuple进行切片，从头开始，到最后结束，步长1
my_list = (0,1,2,3,4,5,6)
result = my_list[:]   # 起始和结束不写表示从头到尾，步长默认为1，可以省略不写
print(f"{result}")

# 对string进行切片，从头开始，到最后结束，步长2
my_list = "01234567"
result = my_list[::2]   # 起始和结束不写表示从头到尾，步长默认为1，可以省略不写
print(f"{result}")


"""
    反向
"""

# 对list进行切片，从3开始，1结束，步长-1，这里的3和1是指元素的下标索引
my_list = [0,1,2,3,4,5,6]
result = my_list[3:1:-1]   # 步长默认为1，可以省略不写
print(f"{result}")

# 对tuple进行切片，从尾开始，到头结束，步长-2
my_list = (0,1,2,3,4,5,6)
result = my_list[::-2]   # 起始和结束不写表示从头到尾，步长默认为1，可以省略不写
print(f"{result}")

# 对string进行切片，从结尾开始，到开头结束，步长-1
my_list = "01234567"
result = my_list[::-1]   # 等同于将序列反转了
print(f"{result}")