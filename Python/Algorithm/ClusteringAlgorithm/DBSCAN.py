import random
from collections import deque
import math
from matplotlib.pyplot import *

markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p', ',', 'o', 's']  # 绘图图标

pointNum = input("输入随机聚类样本个数：")
E = input("输入邻域E：")
minPts = input("输入最小核心对象数目minPts：")


# 计算距离函数
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 随机产生约100个笛卡尔坐标
all_points = []

for i in range(int(pointNum)):
    randCoord = [random.randint(1, 50), random.randint(1, 50)]
    if randCoord not in all_points:
        all_points.append(randCoord)
print(all_points)


# 取差集函数，在a不在b中
def setDifference(a, b):
    c = a.copy()  # python复制list用copy函数
    for i in range(len(a)):
        for j in range(len(b)):
            if str(a[i]) == str(b[j]):
                c.remove(a[i])
    return c


# 取交集函数
def intersection(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if str(a[i]) == str(b[j]):
                c.append(a[i])
    return c


# 选取邻域内的对象点
def lnE(coreObj, otherObj):
    lTE = []
    for num in range(len(otherObj)):
        d = dist(coreObj, otherObj[num])
        if d <= int(E):
            lTE.append(otherObj[num])
    return lTE


coreObject = []
# 我的想法一个簇， 一个簇的找
# 确定核心对象集，如果该点的E半径内的数目大于minPts则加入核心对象集
for x in range(len(all_points)):
    lessThenE = lnE(all_points[x], all_points)  # 选取邻域内的对象集合
    if len(lessThenE) >= int(minPts):  # 如果小于E的集合的长度大于minPts那么将该点加入核心对象集
        coreObject.append(all_points[x])
print("核心对象集：" + str(coreObject))

notVisited = all_points  # 初始化未访问对象集合
clusterNum = 0  # 初始化聚类簇数
cluster = {}  # 初始化聚类
noise = all_points  # 初始化噪声点
while len(coreObject) is not 0:
    print("###############第" + str(clusterNum + 1) + "次处理###############")
    notVisitedOld = notVisited.copy()  # 利用copy创建未访问的队列
    print("此次尚未访问点" + str(notVisited))
    print("此时的核心对象点集" + str(coreObject))
    randCore = random.sample(coreObject, 1)  # 随机选取对象入队
    print("此时随机选取的核心对象" + str(randCore[0]))
    Q = deque()
    Q.append(randCore[0])  # 将该新对象入队
    notVisited.remove(randCore[0])  # 从尚未访问对象集合中删除该点

    while len(Q) is not 0:
        q = Q.popleft()  # 取出队列中的首个样本
        lessThenE = lnE(q, all_points)
        densityReachable = []  # 定义密度可达点集合！！！！密度可达点是空一热按删除
        if len(lessThenE) >= (int(minPts) - 1):
            densityReachable = intersection(lessThenE, notVisited)  # 取和未访问点的交集，找到所有密度可达
            for i in range(0, len(densityReachable)):
                Q.append(densityReachable[i])  # 将密度可达的样本加入到队列中

            notVisitedTmp = setDifference(notVisited, densityReachable)
            notVisited = notVisitedTmp  # 将所有入队的元素剔除

    clusterNum += 1
    cluster[clusterNum] = setDifference(notVisitedOld, notVisited)  # 该集群的点为
    print("集群" + str(clusterNum) + ":" + str(cluster[clusterNum]))  # 输出集群
    coreObjectTmp = setDifference(coreObject, cluster[clusterNum])  # 更新核心对象集，去除已经聚类成功的点
    coreObject = coreObjectTmp
    noise = setDifference(noise, cluster[clusterNum])
    print("此时的噪声点:" + str(noise))

print("##########################################")
print("##########################################")
print("聚类结束:")
print("集合:")
i = 1
for n in range(1, clusterNum + 1):
    print("集群" + str(n) + ":" + str(cluster[n]))  # 输出集群
    clusterx = []
    clustery = []
    for value in cluster[n]:
        clusterx.append(value[0])
        clustery.append(value[1])
    plot(clusterx, clustery, markers[i])
    i = i % 10 + 1
print("噪声点:" + str(noise))

# 绘制集群


noisex = []
noisey = []
for point in noise:
    noisex.append(point[0])
    noisey.append(point[1])
plot(noisex, noisey, "x")

title(str(len(cluster)) + " clusters created with E =" + str(E) + " Min Points=" + str(
    minPts) + " total points=" + str(len(all_points)) + " noise Points = " + str(len(noise)))
axis((0, 60, 0, 60))
show()
