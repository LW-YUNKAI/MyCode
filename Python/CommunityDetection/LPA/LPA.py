# coding=utf-8
import collections
import random
from functools import wraps
import networkx as nx
import time

from util.Modularity import cal_Q
from util.graphDealer import load_graph
from util.timer import fn_timer

'''
paper : <<Near linear time algorithm to detect community structures in large-scale networks>>
LPA主要思想是起初每个节点拥有独立的标签，那么网络中有n不同标签，
每次迭代中对于每个节点将其标签更改为其邻接点中出现次数最多的标签，如果这样的标签有多个，则随机选择一个。
通过迭代，直到每个节点的标签与其邻接点中出现次数最多的标签相同，则达到稳定状态，算法结束。
此时具有相同标签的节点即属于同一个社区。
'''


class LPA:
    def __init__(self, G, max_iter=20):
        self._G = G
        self._n = len(G.node)  # number of nodes
        self._max_iter = max_iter

    def can_stop(self):
        # all node has the label same with its most neighbor
        for i in self._G.nodes():
            node = self._G.node[i]
            label = node["label"]
            max_labels = self.get_max_neighbor_label(i)
            if label not in max_labels:
                return False
        return True

    def get_max_neighbor_label(self, node_index):
        m = collections.defaultdict(int)
        for neighbor_index in self._G.neighbors(node_index):
            neighbor_label = self._G.node[neighbor_index]["label"]
            m[neighbor_label] += 1
        max_v = max(m.values())
        return [item[0] for item in m.items() if item[1] == max_v]

    '''asynchronous update'''

    def populate_label(self):
        # random visit
        visitSequence = random.sample(self._G.nodes(), len(self._G.nodes()))
        for i in visitSequence:
            node = self._G.node[i]
            label = node["label"]
            max_labels = self.get_max_neighbor_label(i)
            if label not in max_labels:
                newLabel = random.choice(max_labels)
                node["label"] = newLabel

    def get_communities(self):
        communities = collections.defaultdict(lambda: list())
        for node in self._G.nodes(True):
            label = node[1]["label"]
            communities[label].append(node[0])
        return communities.values()

    @fn_timer
    def execute(self):
        # initial label
        for i in self._G.nodes():
            self._G.node[i]["label"] = i
        iter_time = 0
        # populate label
        while not self.can_stop() and iter_time < self._max_iter:
            self.populate_label()
            iter_time += 1
        return self.get_communities()


if __name__ == '__main__':
    graphNameClu = ['club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', 'dept3', 'facebook',
                    'lesmis', 'polbooks', 'Q1']
    graphName = input("请输入数据集名('club', 'dolphin', 'football', 'power', 'sciencenet', 'test', 'test2', 'test3', "
                      "'dept3', 'facebook'):")
    if graphName not in graphNameClu:
        print("error")
    else:
        G = load_graph('../../network/%s.txt' % str(graphName))
        # algorithm = LPA(G)
        # communities = algorithm.execute()
        # for community in communities:
        #     print(community)
        # Q = cal_Q(communities, G)
        # print(str(Q))
        # file_object = open('res/res.txt', 'a')
        # file_object.write(
        #     str(graphName) + '|Q:' + str(Q) + '\n')
        # file_object.close()
        # nx.write_gml(G, 'resver2/%sres.gml' % str(graphName))

        for i in range(100):
            resQ = []
            algorithm = LPA(G)
            communities = algorithm.execute()
            Q = cal_Q(communities, G)
            resQ.append(Q)
            file_object = open('res/res.txt', 'a')
            file_object.write(
                str(graphName) + '|Q:' + str(Q) + '\n')
            file_object.close()


