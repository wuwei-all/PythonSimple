# 函数返回值


def add(x,y):
    result = x + y
    # 通过返回值，将相加的结果返回给调用者
    return result
    # return后面的语句不会执行
    print("today")

# 函数的返回值，可以通过变量接受
Sum = add(5,6)
print(Sum)