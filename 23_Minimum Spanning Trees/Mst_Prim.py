import sys
sys.path.append(r'../19_Fibonacci Heaps')
from FibHeap import *
sys.path.append(r'../22_Elementary Graph Algorithms')
from Graph import *

def comparetor(ListfHeapNode1,ListfHeapNode2):
    if ListfHeapNode1.key.key[1] > ListfHeapNode2.key.key[1]:
        return 1
    elif ListfHeapNode1.key.key[1] == ListfHeapNode2.key.key[1]:
        return 0
    else:
        return -1
def PrintDir(Dir):
    for (k,v) in Dir.items():
        print k,
        print v.prev,
        print v.next,
        print 
def mst_prim(G,r):
    FibHeapob = FibHeap(comparetor)
    SetDirQuery = {}
    for v in G.vertexs:
        if v == r:
            fheapNodeob = FibHeapNode(key = [v,0,None])
        else:
            fheapNodeob = FibHeapNode(key = [v,float('inf'),None])
        SetDirQuery[v] = FibHeapob.Insert(fheapNodeob)    
    MinNode = FibHeapob.ExtractMin()
    while MinNode != None:
        u = MinNode.key.key[0]
        print MinNode.key.key
        del SetDirQuery[u]
        for v in G.edges[u]:
            weight = v[1]
            vertex = v[0]
            if SetDirQuery.has_key(vertex) and weight < FibHeapob.getNodeKey(SetDirQuery[vertex])[1]:
                FibHeapob.DrcreaseKey(SetDirQuery[vertex],[vertex,weight,u])
        MinNode = FibHeapob.ExtractMin()
if __name__ == '__main__':
    vertexs = ['a','b','c','d','e','f','g','h','i']
    edges = {'a':[('b',4),('h',8)],
            'b':[('a',4),('c',8),('h',11)],
            'c':[('b',8),('d',7),('f',4),('i',2)],
            'd':[('c',7),('f',14),('e',9)],
            'e':[('d',9),('f',10)],
            'f':[('c',4),('d',14),('e',10),('g',2)],
            'g':[('f',2),('i',6),('h',1)],
            'h':[('a',8),('b',11),('g',1),('i',7)],
            'i':[('c',2),('g',6),('h',7)]
            }
    # edges = {'a':[('b',4),('h',8)],
            # 'b':[('c',8),('h',11)],
            # 'c':[('d',7),('f',4),('i',2)],
            # 'd':[('e',9),('f',14)],
            # 'e':[('f',10)],
            # 'f':[('g',2)],
            # 'g':[('h',1),('i',6)],
            # 'h':[('i',7)],
            # 'i':[]
            # }
    G = Graph(vertexs,edges)
    mst_prim(G,'a')