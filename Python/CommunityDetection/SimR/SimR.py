from CommunityDetection.util.graphDealer import load_graph


def similarity(Graph, node1, node2, C=0.6, sim=0, level=1):
    print(level)
    print(node1, node2)
    print(sim)
    print("*******************")
    if level > 4:
        return 0
    else:
        if node1 is node2:
            return 1
        else:
            nei1Clu = Graph.neighbors(node1).copy()
            nei2Clu = Graph.neighbors(node2).copy()
            for nei1 in nei1Clu:
                for nei2 in nei2Clu:
                    level += 1
                    sim += similarity(Graph, nei1, nei2, C, sim, level)
                    level -= 1
            return C * sim / (len(nei1Clu) * len(nei2Clu))


if __name__ == '__main__':
    itertime = 1
    G = load_graph('../../network/text4.txt')
    print(similarity(G, 1, 2))
    print(similarity(G, 1, 4))
