"""
    编写猜数字程序
"""
import random


# 设置数字范围
low = 1
high = 100

# 生成随机数字
answer = random.randint(low, high)

# 游戏主循环
while True:
    try:
        # 获取玩家输入
        guess = int(input("请猜一个{}到{}之间的整数：".format(low, high)))

        # 判断玩家猜测结果
        if guess < answer:
            print("猜小了，请再试一次。")
        elif guess > answer:
            print("猜大了，请再试一次。")
        else:
            print("恭喜你，猜对了！")
            break  # 猜对后退出循环
    except ValueError:
        # 如果输入的不是整数，给出提示并重新输入
        print("输入无效，请输入一个整数。")



