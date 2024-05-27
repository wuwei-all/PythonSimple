# 在函数内修改全局变量

num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    num = 500  # 不能实现修改全局变量，因为这个是局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)

# 使用global关键字，在函数内声明 变量为全局变量

"""
代码修改如下即可
def test_b():
    global num
    num = 500  
    print(f"test_b:{num}")
"""




