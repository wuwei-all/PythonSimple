# 元组的定义
tup1 = ()       # tup1和tup2为空元组
tup2 = tuple()
tup3 =(123,"zhangsan",True)
print(f"tup1的类型为：{type(tup1)},内容为：{tup1}")
print(f"tup2的类型为：{type(tup2)},内容为：{tup2}")
print(f"tup3的类型为：{type(tup3)},内容为：{tup3}")


tup4 =("zhangsan")
print(f"tup4的类型为：{type(tup4)},内容为：{tup4}")

# 定义单个元素的元组，需要在后面加‘，’,否则为str类型
tup5 =("zhangsan",)
print(f"tup5的类型为：{type(tup5)},内容为：{tup5}")

# 元组的嵌套
tup6 = ((1,2,3),(4,5,6))
print(f"tup6类型为：{type(tup6)},内容是：{tup6}")

# 元组通过下标索引获取元素



# index查找方法

# 元组中指定元素个数统计，count统计方法

# 元组中元素个数统计，len元组长度方法


# 元组的遍历，while
index = 0
while index < len(tup3):
    print(f"元组的元素有：{tup3[index]}")
    index += 1


print("****************************")
# 元组的遍历。for
for element in tup3:
    print(f"元组的元素有：{element}")

# 元组的元素不能修改，但元组的元素为列表时，列表的内容可以修改
tup7 = (1,2,["zhangsan","lisi"])
print(f"tup7修改前的内容为：{tup7}")
tup7[2][0] = "z"
tup7[2][1] = "j"
print(f"tup7修改后的内容为：{tup7}")

