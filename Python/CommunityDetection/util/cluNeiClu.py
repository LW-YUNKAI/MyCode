from util.whichCluster import whichCluster


def cluNeiClu(thisClu, cluList, graph):
    cluNeiCluList = []
    for point in thisClu:
        for nei in graph.neighbors(point):
            cluFrom = whichCluster(nei, cluList)
            if cluFrom not in cluNeiCluList and cluFrom is not thisClu:
                cluNeiCluList.append(cluFrom)
    return cluNeiCluList
