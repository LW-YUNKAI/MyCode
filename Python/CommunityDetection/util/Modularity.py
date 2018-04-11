"""def cal_Q(partition, G):
    m = len(G.edges(None, False))
    a = []
    e = []
    q = 0.0

    for community in partition:
        t = 0.0
        for node in community:
            t += len(G.neighbors(node))
        a.append(t / (2 * m))

    for community in partition:
        t = 0.0
        for i in range(len(community)):
            for j in range(len(community)):
                if G.has_edge(community[i], community[j]):
                    t += 1.0
        e.append(t / (2 * m))

    for ei, ai in zip(e, a):
        q += (ei - ai ** 2)

    return q"""


# 社团内部边数/网络总边数 - （社团内所有点度数之和/2倍总边数）平方
def cal_Q(partition, G):
    m = len(G.edges())
    a = 0.0
    e = 0.0

    # 计算eii
    for community in partition:
        eii = 0.0
        for i in community:
            for j in community:
                if G.has_edge(i, j):
                    eii += 1
        e += eii / (2 * m)
    # 计算aij的平方
    for community in partition:
        aij = 0.0
        for node in community:
            aij += len(G.neighbors(node))
        a += (aij / (2 * m)) ** 2

    q = e - a
    return q


def cal_local_Q(partition, G):
    # 局部模块度
    pass
