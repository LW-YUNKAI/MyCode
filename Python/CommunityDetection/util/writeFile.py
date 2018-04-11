import networkx as nx

from util.Modularity import cal_Q


def writeFile(cluList, graph, i):
    file_object = open('res/clubRes.txt', 'a')
    file_object.write(str(len(cluList)) + " ," + str(cal_Q(cluList, graph)) + '\n')
    file_object.close()
    nx.write_gml(graph, 'res/test%s.gml' % i)
