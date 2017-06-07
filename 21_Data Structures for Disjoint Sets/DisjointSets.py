class NodeSet:
    def __init__(self,key):
        self.parent = self
        self.rank = 0
        self.keys = key
class DisjointSets:
    def __init__(self):
        pass
    def make_set(self,key):
        return NodeSet(key)
    def _link(self,set1,set2):
        if set1.rank > set2.rank:
            set2.parent = set1
            set1.keys = set1.keys + ',' + set2.keys
            return set2
        else:
            set1.parent = set2
            set2.keys = set2.keys + ',' + set1.keys
            if set1.rank == set2.rank:
                set2.rank = set2.rank + 1
            return set1
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
         
SetDirQuery = {}
SetDirResult = {}

for V in Vertex:
    disjointSet = DisjointSetsOb.make_set(V)
    SetDirQuery[V] = disjointSet
    SetDirResult[V] = disjointSet
for edge in Edge:
    if DisjointSetsOb.find_set(SetDirQuery[edge[0]]) != DisjointSetsOb.find_set(SetDirQuery[edge[1]]):
        DelNodeSet = DisjointSetsOb.union(SetDirQuery[edge[0]],SetDirQuery[edge[1]])
        del SetDirResult[DelNodeSet.keys]

for key,set in SetDirResult.iteritems():
    print set.keys
