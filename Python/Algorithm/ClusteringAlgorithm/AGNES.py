import random
import math
import numpy as np  # 提供矩阵运算
from matplotlib.pyplot import plot, axis, show, title

markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p', ',', 'o', 's']  # 绘制图标
pointNum = input("输入随机聚类样本个数：")
k = input("输入聚类个数k：")

# 随机产生约100个笛卡尔坐标
all_points = []

for i in range(int(pointNum)):
    randCoord = [random.randint(1, 50), random.randint(1, 50)]
    if randCoord not in all_points:
        all_points.append(randCoord)


# 计算距离函数
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 找到最小距离的两个簇
def findMinDis(M):
    minDis = float("inf")  # 表示无穷大
    for x in range(len(M[0])):
        for y in range(len(M[0])):
            if x is not y:
                if M[x][y] < minDis:
                    minDis = M[x][y]
                    minClu = cluster[x]
                    minCluNum = x
                    minCluPlus = cluster[y]
                    minCluPlusNum = y
    return minCluNum, minCluPlusNum, minClu, minCluPlus


# 取并集函数
def union(a, b):
    c = []
    for ui in range(len(a)):
        c.append(a[ui])
    for uj in range(len(b)):
        if str(a[ui]) is not str(b[uj]):
            c.append(b[uj])
    return c


# 计算簇中心函数
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


# 创建距离矩阵函数
def contCluDisMatrix(inputClu):
    cluDisMatrix = np.ones((len(inputClu), len(inputClu)))  # 创建矩阵
    # 初始化聚类簇距离矩阵
    for m in range(len(inputClu)):
        for n in range(len(inputClu)):
            cluDisMatrix[m][n] = int(dist(inputClu[m], inputClu[n]))
            cluDisMatrix[n][m] = cluDisMatrix[m][n]
    return cluDisMatrix


cluster = [[]] * len(all_points)  # 创建具俊簇

# 开始聚类，先将每个点设置成一个簇
for num in range(len(all_points)):
    cluster[num] = [all_points[num]]

print("初始集群" + str(cluster))


clusterNum = len(cluster)
print(clusterNum)

while clusterNum >= int(k) :
    # 计算簇中心
    clusterCenter = []  # 簇中心
    for clusterNum in range(len(cluster)):
        clusterCenter.append(center(cluster[clusterNum]))
    print("簇中心：" + str(clusterCenter))
    # 计算距离矩阵
    cluDisMatrix = contCluDisMatrix(clusterCenter)
    # 找到距离最近的两个聚类簇
    # 记录合并后的新簇，删除元有两个簇，添加新簇
    clu1num, clu2num, clu1, clu2 = findMinDis(cluDisMatrix)
    print("最小距离两个簇：" + str(clu1num) + " " + str(clu2num))
    cluster.pop(clu2num)  # 删除第二个元素
    cluTmp = []
    cluTmp = union(clu1, clu2)  # 记录合并后的新簇，删除元有两个簇，添加新簇
    cluster[clu1num] = cluTmp  # 将第二个合并到第一个中
    print(cluster)
    clusterNum -= 1
    print(cluDisMatrix)

print("##########AGNES结束#############")
for i in range(len(cluster)):
    print("第" + str(i + 1) + "个聚类")
    print(cluster[i])
    clusterx = []
    clustery = []
    for value in cluster[i]:
        clusterx.append(value[0])
        clustery.append(value[1])
    plot(clusterx, clustery, markers[i])

title("K-value:" + str(k) + ", total points:" + str(
    len(all_points)))

axis((0, 60, 0, 60))
show()
