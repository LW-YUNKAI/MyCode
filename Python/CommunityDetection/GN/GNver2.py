import networkx as nx
from util.Modularity import cal_Q
from util.graphDealer import clone_graph, load_graph
from util.timer import fn_timer
from util.writeClu import writeClu


# paper: Community structure in social and biological networks
# 边介数（betweenness）：网络中任意两个节点通过此边的最短路径的数目。
# （1）计算每一条边的边介数；
# （2）删除边界数最大的边；
# （3）重新计算网络中剩下的边的边阶数；
# （4）重复(3)和(4)步骤，直到网络中的任一顶点作为一个社区为止。


class GN:
    def __init__(self, G):
        self._G_cloned = clone_graph(G)
        self._G = G
        self._partition = [[n for n in G.nodes()]]
        self._max_Q = 0.0

    @fn_timer
    def execute(self):
        iterTime = 1
        while len(self._G.edges()) != 0:
            # 找到边介数最大的边，删除边
            maxD = -float('Inf')
            edgeDic = nx.edge_betweenness(self._G)
            for edge in edgeDic:
                thisD = edgeDic.get(edge)
                if thisD > maxD:
                    maxD = thisD
                    removeE = edge
            self._G.remove_edge(removeE[0], removeE[1])
            components = [list(c) for c in list(nx.connected_components(self._G))]
            cur_Q = 0
            if len(components) != len(self._partition):
                cur_Q = cal_Q(components, self._G_cloned)
                if cur_Q > self._max_Q:
                    self._max_Q = cur_Q
                    self._partition = components
                    iterRound = iterTime
                    writeClu(self._G, self._partition)
            print("该轮结束的划分结果:" + str(self._partition))
            print("该轮结束时的模块度Q:" + str(cur_Q))
            print("################第" + str(iterTime) + "轮结束##################")

            iterTime += 1

        print("最大Q值出现在：第" + str(iterRound) + "轮。最大Q值为：" + str(self._max_Q))
        for clu in self._partition:
            print(sorted(clu))

        # file_object = open('res/res.txt', 'a')
        # file_object.write(
        #     str(graphName) + " " + str(iterRound) + '|Q:' + str(self._max_Q) + '|Result:' + str(self._partition) + '\n')
        # file_object.close()


if __name__ == '__main__':
    graphName = input("('club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', "
                      "'dept3', 'facebook'):")
    G = load_graph('../../network/%s.txt' % str(graphName))
    algorithm = GN(G)
    algorithm.execute()
    # nx.write_gml(G, 'res/%sres.gml' % str(graphName))
