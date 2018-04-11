from util.Modularity import cal_Q
from util.cluAssemble import cluAssemble
from util.graphDealer import load_graph
from util.pointNeiClu import pointNeiClu
from util.timer import fn_timer

"""
GD算法
计算重叠社区
"""


class GroupDensityOverlap:
    def __init__(self, graph):
        self.G = graph
        self.nodeList = self.G.nodes()
        self.cluList = []
        self.nodeFree = self.nodeList.copy()
        self.degreeList = {}
        for node in self.G.nodes():
            self.degreeList[node] = len(self.G.neighbors(node))

    @fn_timer
    def execute(self):
        iterTime = 1
        # 先找到clu_num个点作为社团核心点
        clu_num = input("请输入划分个数：")
        for t in range(int(clu_num)):
            self.cluList.append([sorted(self.degreeList.items(), key=lambda item: item[1])[-t - 1][0]])
        # 从剩余点中删除核心点
        for t in self.cluList:
            self.nodeFree.remove(t[0])
        # 先将2个核心成员添加
        print("初始社团" + str(self.cluList))
        # flag = 1
        while len(self.nodeFree) != 0:
            tempQ = -float('Inf')
            for clu in self.cluList:
                # 这轮选择的社团
                cluCopy = clu.copy()
                for point in cluCopy:
                    # 选择这个社团中的点
                    print("    该轮选择点" + str(point))
                    for neighbor in self.G.neighbors(point):
                        # 选择该点的邻居节点
                        print("        该点邻居" + str(neighbor))
                        # 如果该邻居节点未被选择
                        if neighbor in self.nodeFree:
                            print("            该邻居没有被选择")
                            # 查看该邻居节点的相邻社团，如果有其他社团，选择Q增值最大的添加
                            for nei in self.G.neighbors(neighbor):
                                print(nei)
                                for neiClu in self.cluList:
                                    print(neiClu)
                                    if nei in neiClu:
                                        print(nei)
                                        partition = self.cluList.copy()
                                        neiCluCopy = neiClu.copy()
                                        neiCluCopy.append(neighbor)
                                        partition.append(neiClu)
                                        print('p'+str(partition))
                                        # 计算模块度
                                        afterQ = cal_Q(partition, self.G)
                                        if afterQ > tempQ:
                                            tempQ = afterQ
                                            goalCluTo = neiClu
                            print(goalCluTo)
                            goalCluTo.append(neiClu)
                            self.cluList.remove(goalCluTo)
                            print("            该邻居添加后的社团" + str(self.cluList))
                            # print("            该邻居添加后的剩余点" + str(self.nodeFree))
                        else:
                            print("            该邻居已经被选择过了")
            print("################第" + str(iterTime) + "轮结束##################")
            iterTime += 1
            print("该轮结束后的社团" + str(self.cluList))
            print("该轮结束后的剩余点" + str(self.nodeFree))
            break


if __name__ == "__main__":
    graphNameClu = ['club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', 'dept3', 'facebook']
    graphName = input("请输入数据集名('club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', "
                      "'dept3', 'facebook'):")
    if graphName not in graphNameClu:
        print("error")
    else:
        G = load_graph('../../network/%s.txt' % str(graphName))
        this = GroupDensityOverlap(G)
        this.execute()
        # nx.write_gml(G, 'resGDOver1/%sres.gml' % str(graphName))
