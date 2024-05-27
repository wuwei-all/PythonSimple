"""
    传参
"""

def user_info(name,age,gender):
    print(f"姓名是：{name}，年龄是：{age},性别是：{gender}")
# 位置传参
user_info("张三",18,"男")

# 关键字传参
user_info(name = "李四",age = 20,gender="男")
user_info(age = 20, name = "王五",gender="女")
user_info("汪峰",age = 20,gender="男")         # 可以和位置参数混用，位置参数需要在前面

# 缺省参数,默认性别为男
# 默认值的参数定义必须在最后，只能是在后面，不能在前面，如name不行，而age和gender可以
def user_info(name,age,gender="男"):
    print(f"姓名是：{name}，年龄是：{age},性别是：{gender}")

user_info("张学友",60)
user_info("张靓颖",30,"女")

# 不定长参数，有两种方式
# 不定长，位置不定长，*号
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")

user_info(1,2,"zhangsan",True)

# 不定长，关键字不定长，**号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")

user_info(name="zhangsan",age = 18)