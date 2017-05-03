#coding:utf-8
class ArrayDoubleLinkList:
    def __init__(self,n):
        self.next = range(1,n)
        self.next.append(0)
        self.prev = [None] * n
        self.key  = [None] * n
        
        self.L = 0
        self.free = 1
        self.next[self.L] = self.prev[self.L] = 0
        self.size = n
    def ListInsert(self,ItemKey):
        
        x = self.AllocateObject()
        if x != None:
            self.key[x] = ItemKey
            self.next[x] = self.next[self.L]
            self.prev[self.next[self.L]] = x
            self.next[self.L] = x
            self.prev[x] = self.L
            return x
        
        
    def ListDelte(self,x):
        self.next[self.prev[x]] = self.next[x]
        self.prev[self.next[x]] = self.prev[x]
        self.FreeObject(x)
    
    def AllocateObject(self):
        if self.free == self.L: #循环列表，判断是否是指向第一个哨兵元素为终止条件
            print "out of space"
        else:
            x = self.free
            self.free = self.next[self.free]
            return x
    def FreeObject(self,x):
        self.next[x] = self.free
        self.free = x
    
if __name__ == '__main__':
    List = ArrayDoubleLinkList(10)
    Element = [0] * 10
    for i in range(0,9):
        Element[i] = List.ListInsert(i)
    for i in range(0,9):
        List.ListDelte(Element[i])
    
    
    
    print List.next
    print List.key
    print List.prev
    print List.free
    print List.L
        
        
      