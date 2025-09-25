import numpy as np
from sklearn.metrics import r2_score

# 给定数据
x = np.array([6712, 6531, 6400, 6143])
y = np.array([7112, 6831, 6710, 6820])
# y = np.array([6566.92,6394.86,6024.81,6143.54])

# 计算 nRMSE
rmse = np.sqrt(np.mean((y - x) ** 2))
nrmse = rmse / np.mean(y)

# 计算R^2
r2 = r2_score(y, x)
print(r2)
print(rmse)
print(nrmse)

