def cluHasEdge(clu1, clu2, graph):
    for p1 in clu1:
        for p2 in clu2:
            if graph.has_edge(p1, p2):
                return True
    return False
