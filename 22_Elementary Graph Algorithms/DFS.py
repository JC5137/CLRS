#coding:utf-8
from Graph import Graph
class GraphProcess:
    #color:white -1 gray 0 black 1
    def __setAttribute(self,Graph):
        vertexs = Graph.vertexs
        self.time = 0
        self.color = {}
        self.timeSpan = {}
        self.prev = {}
        self.sort_vertex_list = []
        for v in vertexs:
            self.color[v] = -1
            self.prev[v] = None
            self.timeSpan[v] = [None for i in range(2)]
    def dfs(self,Graph):
        self.__setAttribute(Graph)
        vertexs = Graph.vertexs
        for u in vertexs:
            if self.color[u] == -1:
                self.__dfs_visit(Graph,u)
    def __dfs_visit(self,Graph,u):
        self.time = self.time + 1
        self.timeSpan[u][0] = self.time
        self.color[u] = 0
        for v in Graph.edges[u]:
            if self.color[v] == -1:
                self.prev[v] = u
                self.__dfs_visit(Graph,v)
        self.color[u] = 1
        self.time = self.time + 1
        self.timeSpan[u][1] = self.time
        self.sort_vertex_list.append(u)
    def topological_sort(self,graph):
        self.dfs(graph)
        for item in self.sort_vertex_list[::-1]:
            print item.decode('utf-8'),
    def strongly_connected_components(self,graph):
        self.dfs(graph)
        vertexs = graph.vertexs
        edges = graph.edges
        transEdge = {}
        for v in vertexs:
            transEdge[v] = []
        for (u,vertexs) in edges.items():
            for v in vertexs:
                transEdge[v] = u
        transGraph = Graph(self.sort_vertex_list[::-1],transEdge)
        self.dfs(transGraph)
        self.__printStrongly_connected_components()
    def __printStrongly_connected_components(self):
        isIntersect = lambda x,y: True if x[0] <= y[1] and y[0] <= x[1] else False
        comparetimeSpan = [0,0]
        for timeSpanItem in sorted(self.timeSpan.items(),key = lambda item:item[1][0]):
            if not isIntersect(comparetimeSpan,timeSpanItem[1]):
                print 
                comparetimeSpan = timeSpanItem[1]
            print timeSpanItem[0],
if __name__ == '__main__':
    #深度优先搜索实例
    # vertexs = ['u','v','w','x','y','z']
    # edge = {'u':['v','x'],
            # 'v':['y'],
            # 'w':['y','z'],
            # 'x':['v'],
            # 'y':['x'],
            # 'z':['z']
            # }
    #拓扑排序实例
    # vertexs = ['内裤','裤子','腰带','衬衣','领带','夹克','袜子','鞋子','手表']
    # edge = {'内裤':['鞋子','裤子'],
            # '裤子':['鞋子','腰带'],
            # '腰带':['夹克'],
            # '衬衣':['腰带','领带'],
            # '领带':['夹克'],
            # '袜子':['鞋子'],
            # '夹克':[],
            # '鞋子':[],
            # '手表':[]
            # }
    #强连通分量实例
    vertexs = ['a','b','c','d','e','f','g','h']
    edge = {'a':['b'],
            'b':['c','f','e'],
            'c':['d','g'],
            'd':['c','h'],
            'e':['a','f'],
            'f':['g'],
            'g':['f','h'],
            'h':['h']
            }
    Graphob = Graph(vertexs,edge)
    GraphProcessob = GraphProcess()
    GraphProcessob.strongly_connected_components(Graphob)
    
    
    
        