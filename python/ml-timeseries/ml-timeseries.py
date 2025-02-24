pip install numpy

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 생성
N = 600

t = np.arange(0, N, 1).reshape(-1, 1)
t = np.array([t[i] + np.random.rand(1) / 4 for i in range(len(t))])
t = np.array([t[i] - np.random.rand(1) / 7 for i in range(len(t))])
t = np.array(np.round(t, 2))

x1 = np.round((np.random.random(N) * 5).reshape(-1, 1), 2)
x2 = np.round((np.random.random(N) * 5).reshape(-1, 1), 2)
x3 = np.round((np.random.random(N) * 5).reshape(-1, 1), 2)

n = np.round((np.random.random(N) * 2).reshape(-1, 1), 2)

y = np.array(
    [
        (
            (np.log(np.abs(2 + x1[t])) - x2[t - 1] ** 2)
            + 0.02 * x3[t - 3] * np.exp(x1[t - 1])
        )
        for t in range(3, len(t))
    ]
)
y = np.round(y + n[3:], 2)

# 데이터 시각화
plt.plot(t[3:], y)
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Time Series Data")
plt.show()

# 데이터 프레임 생성 및 전처리
dataset = pd.DataFrame(
    np.concatenate((t[3:], x1[3:], x2[3:], x3[3:], y), axis=1),
    columns=["t", "x1", "x2", "x3", "y"],
)

deltaT = np.array([(dataset.t[i + 1] - dataset.t[i]) for i in range(len(dataset) - 1)])
deltaT = np.concatenate((np.array([0]), deltaT))

dataset.insert(1, "∆t", deltaT)

# 데이터 확인
print(dataset.head(3))
