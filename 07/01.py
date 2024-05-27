"""
    演示函数的多返回值
"""
def test_return():
    return 1,"zhangsan",True

x,y,z = test_return()
print(x)
print(y)
print(z)