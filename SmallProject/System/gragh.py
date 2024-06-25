import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('ex.xlsx', sheet_name='Sheet1')  # 假设数据在名为'Sheet1'的工作表中

# 假设你的数据是一个DataFrame，其中一列包含标签，一列包含对应的值
# labels = df['file_name']  # 假设标签列名为'Labels'
sizes = df['file_size']  # 假设值列名为'Values'
# sizes = float(sizes)

# 绘制饼状图
plt.figure(figsize=(8, 8))  # 设置图表大小
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.pie(sizes, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')  # 图表标题
plt.show()  # 显示图表