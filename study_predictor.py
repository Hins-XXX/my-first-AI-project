# 一个超简单的AI入门练习：学习时间与成绩预测

import numpy as np
from sklearn.linear_model import LinearRegression

# 模拟一些学习数据（小时数）
X = np.array([[1], [2], [3], [4], [5]])   # 学习时间
y = np.array([55, 60, 65, 70, 75])        # 成绩

# 创建并训练模型
model = LinearRegression()
model.fit(X, y)

# 预测：学习6小时能考多少分？
prediction = model.predict([[6]])

print(f"学习6小时，预计成绩为：{prediction[0]:.2f} 分")
