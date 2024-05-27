"""
    字典
"""

# 定义字典
my_dict = {}
my_dict1 = dict()
my_dict3 = {"张三":100,"李四":90,"王五":60}
print(f"字典的元素为：{my_dict3}，数据类型为：{type(my_dict3)}")

# 不能定义重复key的字典

# 从字典中基于key获取value
score = my_dict3["张三"]
print(f"张三的成绩是：{score}")

# 定义嵌套字典
stu_score_dict = {
    "张三":{
        "语文":100,
        "数学":100,
        "英语":100
    },"李四":{
        "语文": 90,
        "数学": 70,
        "英语": 60
    }
}
print(f"考试成绩如下：{stu_score_dict}")

# 获取张三的语文成绩
score = stu_score_dict["张三"]["语文"]
print(f"张三的语文成绩为：{score}")
