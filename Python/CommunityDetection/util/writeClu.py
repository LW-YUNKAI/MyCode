# 写入所属社团标号
def writeClu(G, currentCluList):
    cluID = 0
    for item in currentCluList:
        cluID += 1
        for item2 in item:
            G.node[item2]['groupID'] = str(cluID)
    # print(G.nodes(data=True))
