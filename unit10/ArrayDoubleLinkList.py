class ArrayDoubleLinkList:
    def __init__(self,n):
        self.next = [None] * n
        self.prev = [None] * n
        self.key  = [None] * n
        
        self.L = 0
        self.next[self.L] = self.prev[self.L] = 0
        self.size = n
    def ListInsert(self,x,ItemKey):
        self.key[x] = ItemKey
        self.next[x] = self.next[self.L]
        self.prev[self.next[self.L]] = x
        self.next[self.L] = x
        self.prev[x] = self.L
        
        
    def ListDelte(self,x):
        self.next[self.prev[x]] = self.next[x]
        self.prev[self.next[x]] = self.prev[x]
    
    def AllocateObject(self):
        if self.free == None:
            print "out of space"
        else:
            x = self.free
            self.free = next[self.free]
            return x
    def FreeObject(x):
        self.next[x] = free
        self.free = x
    
if __name__ == '__main__':
    List = ArrayDoubleLinkList(10)
    List.ListInsert(1,10)
    List.ListInsert(2,9)
    List.ListDelte(1)
    List.ListDelte(2)
    
    
    print List.next
    print List.key
    print List.prev
        
        
      