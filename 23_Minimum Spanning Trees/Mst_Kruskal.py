import sys
sys.path.append(r'../21_Data Structures for Disjoint Sets')
from DisjointSets import *
sys.path.append(r'../22_Elementary Graph Algorithms')
from Graph import *

def mat_kruskal(G):
    DisjointSetsOb = DisjointSets()
    minSpanningTree = []
    SetDirQuery = {}
    for v in G.vertexs:
        SetDirQuery[v] = DisjointSetsOb.make_set(v)
    edgeTuple = []
    for (u,vertexs) in G.edges.items():
        for v in vertexs:
            edgeTuple.append((u,v[0],v[1]))
    for edge in sorted(edgeTuple,key = lambda item:item[2]):
        if DisjointSetsOb.find_set(SetDirQuery[edge[0]]) != DisjointSetsOb.find_set(SetDirQuery[edge[1]]):
            minSpanningTree.append((edge[0],edge[1]))
            DisjointSetsOb.union(SetDirQuery[edge[0]],SetDirQuery[edge[1]])
    return minSpanningTree
if __name__ == '__main__':
    vertexs = ['a','b','c','d','e','f','g','h','i']
    # edges = {'a':[('b',4),('h',8)],
            # 'b':[('a',4),('c',8),('h',11)],
            # 'c':[('b',8),('d',7),('f',4),('i',2)],
            # 'd':[('c',7),('f',14),('e',9)],
            # 'e':[('d',9),('f',10)],
            # 'f':[('c',4),('d',14),('e',10),('g',2)],
            # 'g':[('f',2),('i',6),('h',1)],
            # 'h':[('a',8),('g',1),('i',7)],
            # 'i':[('c',2),('g',6),('h',7)]
            # }
    edges = {'a':[('b',4),('h',8)],
            'b':[('c',8),('h',11)],
            'c':[('d',7),('f',4),('i',2)],
            'd':[('e',9),('f',14)],
            'e':[('f',10)],
            'f':[('g',2)],
            'g':[('h',1),('i',6)],
            'h':[('i',7)],
            'i':[]
            }
    G = Graph(vertexs,edges)
    print mat_kruskal(G)
        