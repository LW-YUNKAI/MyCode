# 随机选择长度最短的社团
import random


def ChooseShortest(currentCluList):
    minLen = float('Inf')
    shortestCluList = []
    for item in currentCluList:
        if len(item) < minLen:
            minLen = len(item)
            shortestCluList.append(item)
    return random.sample(shortestCluList, 1)[0]
