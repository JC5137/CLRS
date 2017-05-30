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
    def Search(self,key):
        Node = self.head
        while Node != None and Node.key != key:
            Node = Node.next
        return Node
    def Insert(self,Node):
        Node.next = self.head
        if self.head != None:
            self.head.prev = Node
        self.head = Node
        Node.prev = None
    def Delete(self,Node):
        if Node.prev != None:  #不是第一个元素
            Node.prev.next = Node.next
        else:
            self.head = Node.next
        if Node.next != None:
            Node.next.prev = Node.prev
    def Print(self):
        Node = self.head
        while Node != None:
            print Node.key,
            Node = Node.next
    def Len(self):
        Node = self.head
        while Node != None:
            self.Length = self.Length + 1
            Node = Node.next
        return self.Length


class DoubleLoopLinkListSentinel:
    def __init__(self):
        self.nil = LinkListNode(None)
        self.nil.prev = self.nil.next = self.nil
    def Search(self,k):
        Node = self.nil.next
        while Node != self.nil and Node.key != k:
            Node = Node.next
        return Node
    def Insert(self,Node):
        Node.next = self.nil.next
        self.nil.next.prev = Node
        self.nil.next = Node
        Node.prev = self.nil
    def Delete(self,Node):
        Node.prev.next = Node.next
        Node.next.prev = Node.prev
    def Print(self):
        Node = self.nil.next 
        while Node != self.nil:
            print Node.key.key,
            Node = Node.next
    def Len(self):
        len = 0
        Node = self.nil.next
        while Node != self.nil:
            len = len + 1
            Node = Node.next
        return len
    @classmethod
    def Union(cls,DoubleLinkList1,DoubleLinkList2):
        if DoubleLinkList1 == None:
            return DoubleLinkList2
        elif DoubleLinkList2 == None:
            return DoubleLinkList1
        else:
            List1TailNode = DoubleLinkList1.nil.prev
            List2TailNode = DoubleLinkList2.nil.prev
            
            List1TailNode.next = DoubleLinkList2.nil.next
            DoubleLinkList2.nil.next.prev = List1TailNode
            
            List2TailNode.next = DoubleLinkList1.nil
            DoubleLinkList1.nil.prev = List2TailNode
            return DoubleLinkList1
        
if __name__ == "__main__":
    DoubleListob1 = DoubleLoopLinkListSentinel()
    Link = [0] * 4
    for i in range(0,4):
        Link[i] = LinkListNode(i)
        DoubleListob1.Insert(Link[i])
        
    DoubleListob2 = DoubleLoopLinkListSentinel()
    Link = [0] * 4
    for i in range(0,4):
        Link[i] = LinkListNode(i)
        DoubleListob2.Insert(Link[i])


    # DoubleListob1.ListDelete(Link[1])
    # DoubleListob1.ListDelete(Link[2])

    # print DoubleListob1.ListSearch(3).next.key
    # DoubleListob1.ListPrint()
    # DoubleListob2.ListPrint()
    # print 
    List = DoubleLoopLinkListSentinel.Union(DoubleListob1,DoubleListob2)
    print List.Len()
    

        