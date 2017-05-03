#coding:utf-8
class LinkListNode:
    def __init__(self,key):
        self.prev = None
        self.next = None
        self.key = key

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.Length = 0
    def ListSearch(self,key):
        Node = self.head
        while Node != None and Node.key != key:
            Node = Node.next
        return Node
    def ListInsert(self,Node):
        Node.next = self.head
        if self.head != None:
            self.head.prev = Node
        self.head = Node
        Node.prev = None
    def ListDelete(self,Node):
        if Node.prev != None:  #不是第一个元素
            Node.prev.next = Node.next
        else:
            self.head = Node.next
        if Node.next != None:
            Node.next.prev = Node.prev
    def ListPrint(self):
        Node = self.head
        while Node != None:
            print Node.key,
            Node = Node.next
    def ListLen(self):
        Node = self.head
        while Node != None:
            self.Length = self.Length + 1
            Node = Node.next
        return self.Length
        

class DoubleLinkListSentinel:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.prev = self.nil.next = self.nil
    def ListSearch(self,k):
        Node = self.nil.next
        while Node != self.nil and Node.key != k:
            Node = Node.next
        return Node
    def ListInsert(self,Node):
        Node.next = self.nil.next
        self.nil.next.prev = Node
        self.nil.next = Node
        Node.prev = self.nil
    def ListDelete(self,Node):
        Node.prev.next = Node.next
        Node.next.prev = Node.prev
    def ListPrint(self):
        Node = DoubleListob.nil.next 
        while Node != DoubleListob.nil:
            print Node.key
            Node = Node.next
        
if __name__ == "__main__":
    DoubleListob = DoubleLinkListSentinel()
    Link = [0] * 4
    for i in range(0,4):
        Link[i] = LinkListNode(i)
        DoubleListob.ListInsert(Link[i])


    DoubleListob.ListDelete(Link[1])
    DoubleListob.ListDelete(Link[2])

    print DoubleListob.ListSearch(3).next.key

    Node = DoubleListob.nil.next 
    while Node != DoubleListob.nil:
        print Node.key
        Node = Node.next

        