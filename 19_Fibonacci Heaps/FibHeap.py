#coding:utf-8
import sys
import math
sys.path.append(r'../10_Elementary Data Structures')
from DoubleLinkList import *
import logging

class FibHeapNode:
    def __init__(self,key = None,parent = None,child = None,degree = 0,mark = False):
        self.key = key
        self.parent = parent
        self.child = child
        self.degree = degree
        self.mark = mark
def comparetor(ListfHeapNode1,ListfHeapNode2):
    if ListfHeapNode1.key.key > ListfHeapNode2.key.key:
        return 1
    elif ListfHeapNode1.key.key == ListfHeapNode2.key.key:
        return 0
    else:
        return -1
class FibHeap:
    @classmethod
    def Union(cls,FibHeap1,FibHeap2):
        NewFibHeap = FibHeap(FibHeap1.comparetor)
        NewFibHeap.n = FibHeap1.n + FibHeap2.n
        NewFibHeap.min = FibHeap1.min
        NewFibHeap.rootList = DoubleLoopLinkListSentinel.Union(FibHeap1.rootList,FibHeap2.rootList)
        if FibHeap1.min == None or (FibHeap2.min != None and FibHeap2.min.key < FibHeap1.min.key):
            NewFibHeap.min = FibHeap2.min
        return NewFibHeap
    @classmethod
    def setParent(cls,ListNode,ParentNode):
        ListNode.key.parent = ParentNode
    @classmethod
    def setChildList(cls,ListNode,ChildList):
        ListNode.key.child = ChildList
    @classmethod
    def ListNodeDegreeIncrement(cls,ListNode):
        ListNode.key.degree = ListNode.key.degree + 1
    @classmethod
    def ListNodeDegreeDecrement(cls,ListNode):
        ListNode.key.degree = ListNode.key.degree - 1
    @classmethod
    def setNodeKey(cls,ListNode,key):
        ListNode.key.key = key
    @classmethod
    def setListNodeMark(cls,ListNode,mark):
        ListNode.key.mark = mark
    #comparetor(a,b) £á> b return 1   a = b return 0 a < b return -1
    def __init__(self,comparetor = comparetor):
        self.min = None
        self.n = 0
        self.comparetor = comparetor
        self.rootList = DoubleLoopLinkListSentinel()
        
        self.getParent = lambda ListNode : ListNode.key.parent
        self.getChildList  = lambda ListNode : ListNode.key.child
        self.getFirstChild = lambda ChildList : ChildList.nil.next
        self.getListNodeDegree = lambda ListNode : ListNode.key.degree
        self.getNodeKey = lambda ListNode : ListNode.key.key
        self.getListNodeMark = lambda ListNode : ListNode.key.mark
    def Insert(self,fHeapNode):
        ListfHeapNode = LinkListNode(fHeapNode)
        self.rootList.Insert(ListfHeapNode)
        self.n = self.n + 1
        if self.min == None:
            self.min = ListfHeapNode
        elif self.comparetor(self.min,ListfHeapNode) == 1:
            self.min = ListfHeapNode
        return ListfHeapNode
    def ExtractMin(self):
        MinNode = self.min
        if MinNode != None:
            for MinNodeChild in self.__FindChildNodes(MinNode): 
                self.rootList.Insert(MinNodeChild) 
                MinNodeChild.parent = None
            self.rootList.Delete(MinNode)
            if self.rootList.Len() == 0: 
                self.min = None
            else:
                self.min = self.min.next
                self.Consolidate()
            self.n = self.n - 1
        return MinNode
    def __FindChildNodes(self,Node):
        childList = self.getChildList(Node)
        if childList == None:
            return []
        else:
            childNode = self.getFirstChild(childList)
            childNodesList = []
            while childNode != childList.nil:
                childNodesList.append(childNode)
                childNode = childNode.next
            return childNodesList
    def Consolidate(self):
        DegreeArraySize = int (math.log(self.n,2) ) + 1
        DegreeArray = [ None for i in range(DegreeArraySize) ]
        Node = self.getFirstChild(self.rootList)
        while Node != self.rootList.nil:
            LittleNode = Node
            degree = self.getListNodeDegree(LittleNode)
            nodeNext = Node.next
            while degree < DegreeArraySize and DegreeArray[degree] != None:
                LargeNode = DegreeArray[degree]
                if self.comparetor(LittleNode,LargeNode) == 1:
                    LittleNode,LargeNode = LargeNode,LittleNode
                self.__HeapLink(LargeNode,LittleNode)
                DegreeArray[degree] = None
                degree = degree + 1
            DegreeArray[degree] = LittleNode
            Node = nodeNext
        self.min = None
        for degree in range(DegreeArraySize):
            if DegreeArray[degree] != None:
                if self.min == None:
                    self.rootList = DoubleLoopLinkListSentinel()
                    self.rootList.Insert(DegreeArray[degree])
                    self.min = DegreeArray[degree]
                else:
                    self.rootList.Insert(DegreeArray[degree])
                    if self.comparetor(self.min,DegreeArray[degree]) == 1:
                        self.min = DegreeArray[degree]
    def __HeapLink(self,LargeNode,LittleNode):
        self.rootList.Delete(LargeNode)
        FibHeap.setParent(LargeNode,LittleNode)
        childList = self.getChildList(LittleNode)
        if childList != None:
            childList.Insert(LargeNode)
        else:
            NewChildList = DoubleLoopLinkListSentinel()
            NewChildList.Insert(LargeNode)
            FibHeap.setChildList(LittleNode,NewChildList)
        FibHeap.ListNodeDegreeIncrement(LittleNode)
        FibHeap.setListNodeMark(LargeNode,False)
    def DrcreaseKey(self,Node,key):
        if self.comparetor(LinkListNode(FibHeapNode(key = key)),Node) == 1:
            print "Exception: new key is greater/less than the current key"
        FibHeap.setNodeKey(Node,key)
        NodeParent = self.getParent(Node)
        if NodeParent != None and self.comparetor(Node,NodeParent) == -1:
            self.__Cut(Node,NodeParent)
            self.__CascadingCut(NodeParent)
        if self.comparetor(Node,self.min) == -1:
            self.min = Node
    def __Cut(self,Node,NodeParent):
        ChildList = self.getChildList(self.getParent(Node))
        ChildList.Delete(Node)
        FibHeap.ListNodeDegreeDecrement(self.getParent(Node))
        self.rootList.Insert(Node)
        FibHeap.setParent(Node,None)
        FibHeap.setListNodeMark(Node,False)
    def __CascadingCut(self,NodeParent):
        NodeGrandParent = self.getParent(NodeParent)
        if NodeGrandParent != None:
            if self.getListNodeMark(NodeParent) == False:
                FibHeap.setListNodeMark(NodeParent,True)
            else:
                self.__Cut(NodeParent,NodeGrandParent)
                self.__CascadingCut(NodeGrandParent)
    def PrettyPrint(self,childList,NumTab):
        if childList != None:
            Node = self.getFirstChild(childList)
            while Node != childList.nil:
                print '----' * NumTab + str(self.getNodeKey(Node))
                self.PrettyPrint(self.getChildList(Node),NumTab + 1)
                Node = Node.next
if __name__ == '__main__':
    FibHeapob = FibHeap()
    FibHeapNodeList = []
    for i in range(10):
        FibHeapNodeList.append(FibHeapNode(i))
        FibHeapob.Insert(FibHeapNodeList[i])
    FibHeapListNodeList = []
    Node = FibHeapob.getFirstChild(FibHeapob.rootList)
    while Node != FibHeapob.rootList.nil:
        FibHeapListNodeList.append(Node)
        Node = Node.next

    for i in range(1):
        FibHeapob.ExtractMin()
    for i in range(0,4):
        FibHeapob.DrcreaseKey(FibHeapListNodeList[i],FibHeapob.getNodeKey(FibHeapListNodeList[i]) - 10)
    FibHeapob.PrettyPrint(FibHeapob.rootList,0)
    
    
    
    
            
        
    
        
        
                
            
            
        