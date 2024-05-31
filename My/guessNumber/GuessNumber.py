"""
    编写猜数字程序
"""
import random


randon_number = random.randint(1,10)

while True:
    guess = int(input("请输入整数："))
    print(f"你输入的数字为：{guess}")
    if guess == randon_number:
        print("恭喜你，猜数正确")
        break
    elif guess > randon_number:
        print("数字大了")
        continue
    else:
        print("数字小了")
        continue

