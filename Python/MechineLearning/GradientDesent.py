import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# y=2 * (x1) + (x2) + 3
figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')

p = [np.random.normal(), np.random.normal(), np.random.normal()]
print("初始随机参数：" + str(p))
iterTime = 0
rate = 0.001

x_train = np.array([[1, 2], [2, 1], [2, 3], [3, 5], [1, 3], [4, 2], [7, 3], [4, 5], [11, 3], [8, 7]])
x_train1 = np.array([xi[0] for xi in x_train])
x_train2 = np.array([xi[1] for xi in x_train])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test = np.array([[1, 4], [2, 2], [2, 5], [5, 3], [1, 5], [4, 1]])


def h(p, x):
    a, b, c = p
    return a * x[0] + b * x[1] + c


# oldJ = -100000
# print(oldJ)
while True:

    sum_a = 0
    sum_b = 0
    sum_c = 0
    m = 1
    J = 0
    for x, y in zip(x_train, y_train):
        sum_a += (h(p, x) - y) * x[0]
        sum_b += (h(p, x) - y) * x[1]
        sum_c += (h(p, x) - y)
        m += 1
        J += (h(p, x) - y) ** 2
    J = J / (2 * m)
    # print(J)
    # temp = abs(J - oldJ)
    p[0] = p[0] - rate / m * sum_a
    p[1] = p[1] - rate / m * sum_b
    p[2] = p[2] - rate / m * sum_c

    if J < 10 ** (-3):
        # print(temp)
        break
    thisY = np.array([h(p, xi) for xi in x_train])
    ax.plot(x_train1, x_train2, thisY)
    iterTime += 1
    # oldJ = J

print(iterTime)
print("拟合参数：" + str(p))
result = [h(p, xi) for xi in x_test]
print(result)

plt.show()
