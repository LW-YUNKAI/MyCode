import numpy as np
import matplotlib.pyplot as plt

path = "data/iris.data"
x_train = []
x_train2 = []
Iris_setosa1 = []
Iris_setosa2 = []
Iris_versicolor1 = []
Iris_versicolor2 = []
Iris_virginica1 = []
Iris_virginica2 = []
markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p', ',', 'o', 's']
y_train = []
with open(path) as text:
    for line in text:
        vertices = line.strip().split(",")
        print(vertices)
        if vertices[4] == 'Iris-setosa':
            Iris_setosa1.append(float(vertices[0]) * float(vertices[1]))
            Iris_setosa2.append(float(vertices[2]) * float(vertices[3]))
            y_train.append(0)
        if vertices[4] == 'Iris-versicolor':
            Iris_versicolor1.append(float(vertices[0]) * float(vertices[1]))
            Iris_versicolor2.append(float(vertices[2]) * float(vertices[3]))
            y_train.append(1)
        if vertices[4] == 'Iris-virginica':
            Iris_virginica1.append(float(vertices[0]) * float(vertices[1]))
            Iris_virginica2.append(float(vertices[2]) * float(vertices[3]))
            y_train.append(2)
        x_train.append([float(vertices[0]), float(vertices[1]), float(vertices[2]), float(vertices[3])])
plt.plot(Iris_setosa1, Iris_setosa2, markers[0])
plt.plot(Iris_versicolor1, Iris_versicolor2, markers[1])
plt.plot(Iris_virginica1, Iris_virginica2, markers[2])
plt.show()


def g(z):
    return 1 / (1 + np.math.e ** (-z))
    pass


def h(theta, x):
    return g(theta * x)
    pass


#
#
# def J(theta, x, y):
#     return (1/m)*Cost()
#
#
p = [np.random.normal(), np.random.normal(), np.random.normal(), np.random.normal(), np.random.normal()]

while True:
    sum_theta0 = 0
    sum_theta1 = 0
    sum_theta2 = 0
    sum_theta3 = 0
    sum_theta4 = 0
    for x, y in zip(x_train, y_train):
        sum_theta0 += (h(p, x) - y) * x
        sum_theta1 += (h(p, x) - y) * x
        sum_theta2 += (h(p, x) - y) * x
        sum_theta3 += (h(p, x) - y) * x
        sum_theta4 += (h(p, x) - y) * x
        # print("初始随机参数："+str(p))
        # # 迭代次数
        # iterTime = 1000
        # # 步长
        # rate = 0.01
        #
        # # x坐标，y坐标
        # x_train = np.array([1, 2, 3, 4, 7, 11, 8, 30])
        # y_train = np.array([7, 9, 11, 13, 19, 27, 21, 65])
        # x_test = np.array([12, 18, 20])
        #
        #
        # def h(p, x0):
        #     theta0, theta1 = p
        #     return theta1 * x0 + theta0
        #
        #
        # for i in range(iterTime):
        #     # 进行1000次迭代
        #     sum_theta0 = 0
        #     sum_theta1 = 0
        #     m = 1
        #     for x, y in zip(x_train, y_train):
        #         # theta1求导结果之和
        #         sum_theta1 += (h(p, x) - y) * x
        #         # theta2求导结果之和
        #         sum_theta0 += (h(p, x) - y)
        #         m += 1
        #     # 计算新的拟合参数
        #     p[0] = p[0] - rate/m*sum_theta0
        #     p[1] = p[1] - rate/m*sum_theta1
        #
        #     plt.plot(x_train, h(p, x_train))
        #
        # print("拟合参数："+str(p))
        #
        # result = [h(p, xi) for xi in x_test]
        # print(result)
