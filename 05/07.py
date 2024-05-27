"""
    演示特殊字面量：None
"""

# 无return语句的函数返回值,显示内容为None
def say_hi():
    print("hello")

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

print("*******************************")

# 主动返回为None
def say_hi1():
    print("hello")
    return None

result = say_hi1()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

# None用于声明无初始值内容的变量
name = None