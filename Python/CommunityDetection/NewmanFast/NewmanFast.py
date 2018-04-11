import random
import networkx as nx
from util.Modularity import cal_Q
from util.cluHasEdge import cluHasEdge
from util.graphDealer import load_graph
from util.timer import fn_timer
from util.writeClu import writeClu


# newman快速算法


# 随机选择长度最短的社团
def ChooseShortest(currentCluList):
    minLen = float('Inf')
    shortestCluList = []
    for item in currentCluList:
        if len(item) < minLen:
            minLen = len(item)
            shortestCluList.append(item)
    return random.sample(shortestCluList, 1)[0]


# 随机选择Q最小的社团
def ChooseSmallestQ(currentCluList, graph):
    minLen = float('Inf')
    shortestCluList = []
    for item in currentCluList:
        if cal_Q(currentCluList, graph) < minLen:
            minLen = len(item)
            shortestCluList.append(item)
    return random.sample(shortestCluList, 1)


# 合并社团
def cluAssemble(self, other, currentCluList):
    currentCluList.remove(self)
    currentCluList.remove(other)
    for node in self:
        if node not in other:
            other.append(node)
    currentCluList.append(other)
    cluAfterAssemble = currentCluList
    return cluAfterAssemble


class newmanFast:
    def __init__(self, graph):
        self.G = graph
        self.nodeList = self.G.nodes()
        self.cluList = []
        for i in self.nodeList:
            self.cluList.append([i])
        self.finalClu = []

    @fn_timer
    def execute(self):
        iterTime = 1
        # 先将每个节点看作一个社区，然后选择模块度增值最大的进行合并，直到所有社团变成一个社团为止
        # print(self.cluList)
        maxQ = -float('Inf')
        # 只要社团列表长度不为1
        while len(self.cluList) is not 1:
            Q = -float('Inf')
            # 随机选择一个最小社团
            for cluFrom in self.cluList:
                thisClu = self.cluList.copy()
                thisClu.remove(cluFrom)
                for cluTo in thisClu:
                    if cluHasEdge(cluFrom, cluTo, self.G):
                        partition = cluAssemble(cluFrom.copy(), cluTo.copy(), self.cluList.copy())
                        thisQ = cal_Q(partition, self.G)
                        # print("社团" + str(cluTo) + "q值" + str(thisQ))
                        # 记录该轮最大Q和目标社团
                        if thisQ >= Q:
                            Q = thisQ
                            finalCluFrom = cluFrom
                            finalCluTo = cluTo
            # print("finalCluFrom" + str(finalCluFrom))
            # print("finalCluTo" + str(finalCluTo))

            cluAssemble(finalCluFrom.copy(), finalCluTo.copy(), self.cluList)
            print("该轮结束的划分结果:" + str(self.cluList))
            # print("该轮结束时的模块度Q:" + str(Q))
            print("################第" + str(iterTime) + "轮结束##################")
            # file_object = open('res/%sres.txt' % str(graphName), 'a')
            # file_object.write(str(iterTime) + '|Q:' + str(Q) + '|Result:' + str(self.cluList) + '\n')
            # file_object.close()

            iterTime += 1
            if Q > maxQ:
                maxQ = Q
                iterRound = iterTime - 1
                self.finalClu = self.cluList.copy()
                writeClu(self.G, self.cluList)

        print("最大Q值出现在：第" + str(iterRound) + "轮。最大Q值为：" + str(maxQ))
        for clu in self.finalClu:
            print(sorted(clu))
        # file_object = open('res/res.txt', 'a')
        # file_object.write(str(graphName) + ' ' + str(iterRound) + '|Q:' + str(maxQ) + '|Result:' + str(
        #     self.finalClu) + '\n')
        # file_object.close()


if __name__ == "__main__":
    graphNameClu = ['club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', 'facebook',
                    'lesmis', 'polbooks', 'jazz']
    graphName = input("'club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', 'facebook',"
                      "'lesmis', 'polbooks', 'jazz', 'facebook'):")
    if graphName not in graphNameClu:
        print("error")
    else:
        G = load_graph('../../network/%s.txt' % str(graphName))
        this = newmanFast(G)
        this.execute()
        # nx.write_gml(G, 'res/%sres.gml' % str(graphName))
