"""
    字典的常见操作
"""
my_dict = {"张三":100,"李四":90,"王五":60}

# 新增字典元素
my_dict["赵六"] = 66
print(f"新增后字典的元素为：{my_dict}")

# 更新字典元素
my_dict["张三"] = 99
print(f"更新字典元素后，结果{my_dict}")

# 删除元素
score = my_dict.pop("张三")
print(f"字典中删除元素，结果{my_dict},张三的成绩为：{score}")

# 获取全部的key
keys = my_dict.keys()
print(f"字典全部的key，结果：{keys}")

# 遍历字典
# 方法一：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

print("**********************")
# 方法二：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

print("**********************")

# 统计字典的元素个数

# 清空字典
my_dict.clear()
print(f"字典清空后，结果:{my_dict}")