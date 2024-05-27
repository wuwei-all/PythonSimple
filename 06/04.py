"""
    列表的相关炒作
"""

# 查询列表指定元素的下标
my_list = ["zhangsan","lisi","wangwu"]
index = my_list.index("zhangsan")
print(f"zhangsan在列表的位置为：{index}")

# 修改指定下标的元素值
my_list[0] = "zj"
print(f"my_list修改后的值为:{my_list}")

# 在指定下标中插入元素
my_list.insert(1,"good")
print(f"my_list插入元素后的值：{my_list}")

# 将单个指定元素，追加到列表的尾部
my_list.append("666")
print(f"my_list追加单个元素后，结果：{my_list}")

# 将多个指定元素，追加到列表的尾部
my_list1 = ["hello",123,True]
my_list.extend(my_list1)
print(f"my_list追加多个元素后，结果：{my_list}")

# 删除指定下标的元素值，有两种方式
# 方法一
del my_list[0]
print(f"列表删除后的结果是：{my_list}")

# 方法二，pop可以获取删除的值，而del没有这个功能
element = my_list.pop(0)
print(f"通过POP方法取出元素后的类别内容是：{my_list},取出的元素是：{element}")


# 删除某元素在列表中的第一个匹配项，remove

# 统计列表中指定元素的个数，count
sum = my_list.count("lisi")
print(f"在my_list列表中lisi的个数为：{sum}")

# 统计列表中一共有多少个元素,len
sum = len(my_list)
print(f"my_list一共有：{sum}个元素")

# 清空列表内容，clear
my_list.clear()
print(f"列表清空后，结果为：{my_list}")


