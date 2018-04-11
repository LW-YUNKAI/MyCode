import numpy as np
import matplotlib.pyplot as plt

# y=2 * (x) + 5
# p[theta0, theta1]
p = [np.random.normal(), np.random.normal()]
print("初始随机参数："+str(p))
# 迭代次数
iterTime = 1000
# 步长
rate = 0.01

# x坐标，y坐标
x_train = np.array([1, 2, 3, 4, 7, 11, 8, 30])
y_train = np.array([7, 9, 11, 13, 19, 27, 21, 65])
x_test = np.array([12, 18, 20])


def h(p, x0):
    theta0, theta1 = p
    return theta1 * x0 + theta0


for i in range(iterTime):
    # 进行1000次迭代
    sum_theta0 = 0
    sum_theta1 = 0
    m = 1
    for x, y in zip(x_train, y_train):
        # theta1求导结果之和
        sum_theta1 += (h(p, x) - y) * x
        # theta2求导结果之和
        sum_theta0 += (h(p, x) - y)
        m += 1
    # 计算新的拟合参数
    p[0] = p[0] - rate/m*sum_theta0
    p[1] = p[1] - rate/m*sum_theta1

    plt.plot(x_train, h(p, x_train))

print("拟合参数："+str(p))

result = [h(p, xi) for xi in x_test]
print(result)

plt.show()
