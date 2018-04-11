# 返回点所属社团
from util.graphDealer import load_graph
from util.simplifiedNewmanFast import newmanFast


# 自动返回none
def whichCluster(point, currentCluList):
    for item in currentCluList:
        if point in item:
            return item

if __name__ == '__main__':
    G = load_graph('../network/test.txt')
    this = newmanFast(G)
    this.execute()
    print(" ")
