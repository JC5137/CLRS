import sys
sys.path.append(r'../10_Elementary Data Structures')
from MyQueue import Queue

class Graph:
    #color:white -1 gray 0 black 1
    def __init__(self,vertexs,edges):
        self.vertexs = vertexs
        self.edges = edges
        self.__setAttribute()
    def __setAttribute(self):
        self.color = {}
        self.distance = {}
        self.prev = {}
        for v in vertexs:
            self.color[v] = -1
            self.distance[v] = float('inf')
            self.prev[v] = None
    def BFS(self,start):
        self.__setAttribute()
        self.color[start] = 0
        self.distance[start] = 0
        self.prev[start] = None
        Q = Queue(len(self.vertexs))
        Q.EnQueue(start)
        while not Q.IsEmpty():
            u = Q.DeQueue()
            for v in self.edges[u]:
                if self.color[v] == -1:
                    self.color[v] = 0
                    self.distance[v] = self.distance[u] + 1
                    self.prev[v] = u
                    Q.EnQueue(v)
            self.color[u] = 1
    def PrintPath(self,start,vertex):
        if start == vertex:
            print start,
        elif self.prev[vertex] == None:
            print "No Path"
        else:
            self.PrintPath(start,self.prev[vertex])
            print vertex,
            
     
if __name__ == '__main__':
    vertexs = ['r','s','t','u','v','w','x','y']
    edge = {'r':['s','v'],
            's':['r','w'],
            't':['u','w','x'],
            'u':['t','x','y'],
            'v':['r'],
            'w':['s','t','x'],
            'x':['t','w','y'],
            'y':['u','x']
            }
    Graphob = Graph(vertexs,edge)
    Graphob.BFS('s')
    print Graphob.prev
    print Graphob.distance
    Graphob.PrintPath('s','v')