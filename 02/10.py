# 字符串和数字的拼接，通过占位的形式
name = "zhangjie"
age = 20
number = 110.0
message = "我的姓名是：%s，年龄是：%s，手机号码是：%s" %(name,age,number)
print(message)

message1 = "我的姓名是：%s，年龄是：%d，手机号码是：%f" %(name,age,number)
print(message1)