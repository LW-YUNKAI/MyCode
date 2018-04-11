# newman快速算法
from util.Modularity import cal_Q
from util.cluAssemble import cluAssemble
from util.cluHasEdge import cluHasEdge
from util.graphDealer import load_graph
from util.writeClu import writeClu


class newmanFast:
    def __init__(self, graph):
        self.G = graph
        self.nodeList = self.G.nodes()
        self.cluList = []
        for i in self.nodeList:
            self.cluList.append([i])
        self.finalClu = []

    def execute(self):
        iterTime = 1
        maxQ = -float('Inf')
        # 只要社团列表长度不为1
        while len(self.cluList) is not 1:
            Q = -float('Inf')
            for cluFrom in self.cluList:
                thisClu = self.cluList.copy()
                thisClu.remove(cluFrom)
                for cluTo in thisClu:
                    if cluHasEdge(cluFrom, cluTo, self.G):
                        partition = cluAssemble(cluFrom.copy(), cluTo.copy(), self.cluList.copy())
                        thisQ = cal_Q(partition, self.G)
                        if thisQ >= Q:
                            Q = thisQ
                            finalCluFrom = cluFrom
                            finalCluTo = cluTo
            cluAssemble(finalCluFrom.copy(), finalCluTo.copy(), self.cluList)
            print("该轮结束的划分结果:" + str(self.cluList))
            print("该轮结束时的模块度Q:" + str(Q))
            print("################第" + str(iterTime) + "轮结束##################")
            iterTime += 1
            if Q > maxQ:
                maxQ = Q
                iterRound = iterTime - 1
                self.finalClu = self.cluList.copy()
                writeClu(self.G, self.cluList)

        print("最大Q值出现在：第" + str(iterRound) + "轮。最大Q值为：" + str(maxQ))
        for clu in self.finalClu:
            print(sorted(clu))


if __name__ == "__main__":
    graphNameClu = ['club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', 'dept3', 'facebook']
    graphName = input("请输入数据集名('club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', "
                      "'dept3', 'facebook'):")
    if graphName not in graphNameClu:
        print("error")
    else:
        G = load_graph('../network/%s.txt' % str(graphName))
        this = newmanFast(G)
        this.execute()
