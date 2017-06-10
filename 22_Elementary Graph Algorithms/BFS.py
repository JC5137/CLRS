import sys
sys.path.append(r'../10_Elementary Data Structures')
from MyQueue import Queue
from Graph import Graph
class GraphProcess:
    #color:white -1 gray 0 black 1
    def __setAttribute(self,Graph):
        self.color = {}
        self.distance = {}
        self.prev = {}
        for v in Graph.vertexs:
            self.color[v] = -1
            self.distance[v] = float('inf')
            self.prev[v] = None
    def BFS(self,Graph,start):
        self.__setAttribute(Graph)
        self.color[start] = 0
        self.distance[start] = 0
        self.prev[start] = None
        Q = Queue(len(Graph.vertexs))
        Q.EnQueue(start)
        while not Q.IsEmpty():
            u = Q.DeQueue()
            for v in Graph.edges[u]:
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
    edges = {'r':['s','v'],
            's':['r','w'],
            't':['u','w','x'],
            'u':['t','x','y'],
            'v':['r'],
            'w':['s','t','x'],
            'x':['t','w','y'],
            'y':['u','x']
            }
    Graphob = Graph(vertexs,edge)
    GraphProcessob = GraphProcess()
    GraphProcessob.BFS(Graphob,'s')
    print GraphProcessob.prev
    print GraphProcessob.distance
    GraphProcessob.PrintPath('s','v')