# 已知多条近似交汇于同一个点的直线，想求解出一个近似交点：寻找到一个距离所有直线距离平方和最小的点，该点即最小二乘解；
# 已知多个近似分布于同一直线上的点，想拟合出一个直线方程：设该直线方程为y=kx+b，调整参数k和b，使得所有点到该直线的距离平方之和最小
# 求导
import matplotlib.pyplot as plt
from sympy import diff, Symbol


def func(p, x):
    a, b, c = p
    return a * (x ** 2) + b * x + c


def di(p, x, ci):
    X =Symbol("x")
    return diff(func(p, X), X)


if __name__ == '__main__':
    p0 = [1, 2, 3]
    Xi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 16, 19]
    Yi = []
    Di = []
    for xi in Xi:
        y = func(p=p0, x=xi)
        Yi.append(y)
        # d = di(p0, xi, 1)
        # Di.append(d)
    plt.plot(Xi, Yi)
    plt.plot(Xi, Di)
    plt.show()
