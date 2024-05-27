"""
    集合
"""
# 集合的定义
my_set_empty = set()      # 空集合不能定义为my_set_empty = {}，创建后数据类型为字典
print(f"my_set_empty的类型为：{type(my_set_empty)}")

my_set = {"zhangjie","zhangjie","lisi","wangwu"}
print(f"集合会保留一个相同的元素，其他的删除，集合的内容是去重并且无序的，my_set的内容是：{my_set}")
print(f"my_set的类型是：{type(my_set)}")

# 集合不支持下标索引

# 添加新元素
my_set.add("666")
print(f"添加后的集合：{my_set}")

# 移除元素
my_set.remove("666")
print(f"集合移除666的结果为：{my_set}")

# 随机取出一个元素
element = my_set.pop()
print(f"随机取出的元素是：{element},剩下的集合为：{my_set}")

# 清空集合
my_set.clear()
print(f"集合清空的结果为：{my_set}")

# 取两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出 差集后的结果为：{set3}")
print(f"取出差集后，原有set1的结果为：{set1}")
print(f"取出差集后，原有set2的结果为：{set2}")

# 消除两个集合的差集


# 练个集合的合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"两集合合并的结果：{set3}")
print(f"合并的，原有set1的结果为：{set1}")
print(f"合并的，原有set2的结果为：{set2}")

# 统计集合元素的数量

# 集合的遍历
# 集合不支持下标索引，不能使用while循环
set1 = {1,2,3,4,5,6}
for element in set1:
    print(f"集合的元素有：{element}")

