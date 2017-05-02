#coding:utf-8
class LinkListNode:
    def __init__(self,key):
        self.prev = None
        self.next = None
        self.key = key

class DoubleLinkList:
    def __init__(self):
        self.head = None
    def ListSearch(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x
    def ListInsert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
    def ListDelete(self,x):
        if x.prev != None:  #不是第一个元素
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

class DoubleLinkListSentinel:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.prev = self.nil.next = self.nil
    def ListSearch(self,k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x
    def ListInsert(self,x):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil
    def ListDelete(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev
        
if __name__ == "__main__":
    DoubleListob = DoubleLinkListSentinel()
    Link = [0] * 4
    for i in range(0,4):
        Link[i] = LinkListNode(i)
        DoubleListob.ListInsert(Link[i])


    DoubleListob.ListDelete(Link[1])
    DoubleListob.ListDelete(Link[2])

    print DoubleListob.ListSearch(3).next.key

    x = DoubleListob.nil.next 
    while x != DoubleListob.nil:
        print x.key
        x = x.next

        