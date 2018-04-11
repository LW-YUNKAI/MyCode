import random
import math
from matplotlib.pyplot import *

markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p', ',', 'o', 's']  # 绘图图标
pointNum = input("输入随机聚类样本个数：")
k = input("输入聚类个数k：")


# 计算距离函数
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 计算均值向量（中心点）函数
def center(d):
    x = 0
    y = 0
    for iCenter in range(len(d)):
        x += d[iCenter][0]
        y += d[iCenter][1]
    x //= len(d)
    y //= len(d)
    newCenter = [x, y]
    return newCenter


# 随机产生约pointNum个笛卡尔坐标
all_points = []
for i in range(int(pointNum)):
    randCoord = [random.randint(1, 50), random.randint(1, 50)]
    if randCoord not in all_points:
        all_points.append(randCoord)

print(all_points)

# 选取k个样本作为初始均值向量
k_points = []
k_pointsNum = []

while len(k_points) < int(k):
    randK = random.randint(0, int(len(all_points)) - 1)
    if randK not in k_pointsNum:
        k_points.append(all_points[randK])
        k_pointsNum.append(randK)
print("初始向量点:" + str(k_points))

maxIteNum = 1  # 设置最大迭代次数为20
while maxIteNum < 20:
    k_pointsPre = str(k_points)  # 记录上次的均值向量
    print("****************第" + str(maxIteNum) + "次聚类*****************")
    maxIteNum += 1
    print("先前核心向量点" + str(k_pointsPre))
    cluster = {}  # 产生k个初始集群
    for a in range(len(k_points)):  # 将该聚类完全清空重新添加点
        cluster[a] = []

    # 计算初始距离,根据距离最近的向量确定该点的簇标记
    # 找每个点对应的最近进的初始向量
    for i in range(len(all_points)):
        minDis = 10000
        for j in range(len(k_points)):
            distance = dist(all_points[i], k_points[j])
            if distance < minDis:  # 如果该距离不是最小的
                minDis = distance  # 将最小值设置成该距离
                cluBelongTo = j  # 记录该点所属的集群
        cluster[cluBelongTo].append(all_points[i])
    # 得到的是该论划分后的结果
    print(cluster)

    # 计算新的均值向量并更新
    for i in range(len(k_points)):
        newCenter = center(cluster[i])
        if newCenter != k_points[i]:
            k_points[i] = newCenter
    print("该次聚类后的更新核心点" + str(k_points))

    # 如果当前均值向量都没有更新，表示成功！
    if str(k_points) == k_pointsPre:
        print("聚类成功！！")
        for t in range(len(k_points)):
            print("第" + str(t + 1) + "类：" + str(cluster[t]))
            clusterx = []
            clustery = []
            for value in cluster[t]:
                clusterx.append(value[0])
                clustery.append(value[1])
            plot(clusterx, clustery, markers[t])
        break

# 绘制集群
title("K-value:" + str(len(k_points)) + ", total points:" + str(
    len(all_points)) + ", Number of iterations:" + str(maxIteNum))

axis((0, 60, 0, 60))
show()
