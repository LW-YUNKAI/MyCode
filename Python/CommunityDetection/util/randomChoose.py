import random


def randomChoose(currentCluList):
    g = random.randint(0, len(currentCluList) - 1)
    return currentCluList[g]
