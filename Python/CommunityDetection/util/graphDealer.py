import networkx as nx


def load_graph(path):
    G = nx.Graph()
    with open(path) as text:
        for line in text:
            vertices = line.strip().split(" ")
            sourcePoint = int(vertices[0])
            targetPoint = int(vertices[1])
            if G.has_edge(sourcePoint, targetPoint):
                continue
            G.add_edge(sourcePoint, targetPoint)
    return G


def clone_graph(graph):
    clone_g = nx.Graph()
    for edge in graph.edges():
        clone_g.add_edge(edge[0], edge[1])
    return clone_g

if __name__ == "__main__":
    G = load_graph('../network/club.txt')
    print(G.edges())
    print(G.neighbors(0))

