# birch 算法
#
import random
from matplotlib.pyplot import *

markers = ['+', '*', '.', 'd', '^', 'v', '>', '<', 'p', ',', 'o', 's']  # 绘图图标

pointNum = input("输入随机聚类样本个数：")
# 随机产生约pointNum个笛卡尔坐标
all_points = []
for i in range(int(pointNum)):
    randCoord = [random.randint(1, 10), random.randint(1, 10)]
    if randCoord not in all_points:
        all_points.append(randCoord)

print(all_points)


# CF聚类特征,CF是一个字典
def CF(cluster):
    n = len(cluster)
    LS = [0, 0]
    SS = 0
    clusterFeature = {"num":n}
    for point in cluster:
        LS[0] += point[0]
        LS[1] += point[1]
        SS += pow(point[0], 2)
        SS += pow(point[1], 2)
    clusterFeature["LS"] = LS
    clusterFeature["SS"] = SS
    return clusterFeature


print(CF(all_points))
