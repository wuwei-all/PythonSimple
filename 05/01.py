# 统计字符串长度，不使用内置的len函数

str1 = "hello"
str2 = "world"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：",{count})

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是：",{count})


print("*********************************")

# 使用函数实现以上功能
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)