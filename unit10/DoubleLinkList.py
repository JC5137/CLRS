#coding:utf-8
class DoubleLinkList:
    def __init__(self):
        self.head = None
    def ListSearch(self,key):
        x = self.head
        while x != None and x.key != key:
            x = x.next
        return x
    def LinkInsert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None
    def LinkDelete(self,x):
        if x.prev != None:  #不是第一个元素
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev
                   
class LinkListNode:
    def __init__(self,key):
        self.prev = None
        self.next = None
        self.key = key

if __name__ == "__main__":
    DoubleListob = DoubleLinkList()
    Link = [0] * 4
    for i in range(0,4):
        Link[i] = LinkListNode(i)
        DoubleListob.LinkInsert(Link[i])


    DoubleListob.LinkDelete(Link[1])
    DoubleListob.LinkDelete(Link[2])

    print DoubleListob.ListSearch(3).next.key

    x = DoubleListob.head 
    while x != None:
        print x.key
        x = x.next

        