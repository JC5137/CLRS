class NodeSet:
    def __init__(self,key):
        self.parent = self
        self.rank = 0
        self.key = []
        self.key.append(key)
class DisjointSets:
    def __init__(self):
        pass
    def make_set(self,key):
        return NodeSet(key)
    def _link(self,set1,set2):
        if set1.rank > set2.rank:
            set2.parent = set1
            set1.key.extend(set2.key)
            return set1
        else:
            set1.parent = set2
            set2.key.extend(set1.key)
            if set1.rank == set2.rank:
                set2.rank = set2.rank + 1
            return set2
    def union(self,set1,set2):
        return self._link(self.find_set(set1),self.find_set(set2))
    def find_set(self,set):
        if set.parent != set:
            set.parent = self.find_set(set.parent)
        return set.parent
DisjointSetsOb = DisjointSets()

Vertex = ['a','b','c','d','e','f','g','h','i','j']
Edge = [ ('a','b'),('a','c'),('b','a'),('b','c'),('b','d'),('c','a'),('c','b'),
         ('d','b'),('e','f'),('e','g'),('f','e'),('g','e'),('h','i'),('i','h') ]
         
SetDir = {}
DisjointSetsList = []
for V in Vertex:
    SetDir[V] = DisjointSetsOb.make_set(V)
for edge in Edge:
    if DisjointSetsOb.find_set(SetDir[edge[0]]) != DisjointSetsOb.find_set(SetDir[edge[1]]):
        NodeSet = DisjointSetsOb.union(SetDir[edge[0]],SetDir[edge[1]])

    
