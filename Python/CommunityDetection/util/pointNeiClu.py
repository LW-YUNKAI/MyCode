from util.graphDealer import load_graph
from util.simplifiedNewmanFast import newmanFast
from util.whichCluster import whichCluster


# 包含自身的社团
def pointNeiClu(thisPoint, cluList, graph):
    pointNeiCluList = []
    originClu = whichCluster(thisPoint, cluList)
    for nei in graph.neighbors(thisPoint):
        cluFrom = whichCluster(nei, cluList)
        if cluFrom is None:
            continue
        if cluFrom not in pointNeiCluList:
            pointNeiCluList.append(cluFrom)
    return pointNeiCluList


if __name__ == '__main__':
    G = load_graph('../network/test.txt')
    this = newmanFast(G)
    this.execute()
    print(" ")

    for point in this.G:
        print(point)
        print(pointNeiClu(point, this.finalClu, this.G))
