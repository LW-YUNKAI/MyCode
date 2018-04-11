from util.graphDealer import load_graph
from util.simplifiedNewmanFast import newmanFast


# 返回当前社团的邻居节点
def cluNeiPoint(thisClu, graph):
    cluNeiPointList = []
    for point in thisClu:
        for nei in graph.neighbors(point):
            if nei not in thisClu and nei not in cluNeiPointList:
                cluNeiPointList.append(nei)
    return cluNeiPointList


if __name__ == '__main__':
    G = load_graph('../network/test.txt')
    this = newmanFast(G)
    this.execute()
    for clu in this.finalClu:
        cluNeiPList = cluNeiPoint(clu, G)
        print(cluNeiPList)
