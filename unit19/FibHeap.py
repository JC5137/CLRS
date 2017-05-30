#coding:utf-8
import sys
import math
sys.path.append(r'../unit10')
from DoubleLinkList import *

class FibHeapNode:
    def __init__(self,key = None,parent = None,child = None,degree = 0,mark = False):
        self.key = key
        self.parent = parent
        self.child = child
        self.degree = degree
        self.mark = mark
def comparetor(ListfHeapNode1,ListfHeapNode2):
    if ListfHeapNode1.key.key >= ListfHeapNode2.key.key:
        return 1
    else:
        return 0
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
    #comparetor(a,b) £á>= b return 1   a< b return 0
    def __init__(self,comparetor):
        self.min = None
        self.n = 0
        self.comparetor = comparetor
        self.rootList = DoubleLoopLinkListSentinel()
    def Insert(self,fHeapNode):
        ListfHeapNode = LinkListNode(fHeapNode)
        self.rootList.Insert(ListfHeapNode)
        self.n = self.n + 1
        if self.min == None:
            self.min = ListfHeapNode
        elif self.comparetor(self.min,ListfHeapNode) == 1:
            self.min = ListfHeapNode
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
        childList = Node.key.child
        if childList == None:
            return []
        else:
            childNode = childList.nil.next
            childNodesList = []
            while childNode != childNode.nil:
                childNodesList.append(childNode)
                childNode = childNode.next
            return childNodesList
    def Consolidate(self):
        DegreeArray = [ None for i in range(int (math.log(self.n,2)) + 1) ]
        Node = self.rootList.nil.next
        while Node != self.rootList.nil:
            LittleNode = Node
            degree = LittleNode.key.degree
            while degree < len(DegreeArray) and DegreeArray[degree] != None:
                LargeNode = DegreeArray[degree]
                if self.comparetor(LittleNode,LargeNode) == 1:
                    LittleNode,LargeNode = LargeNode,LittleNode
                self.__HeapLink(LargeNode,LittleNode)
                DegreeArray[degree] = None
                degree = degree + 1
            DegreeArray[degree] = LittleNode
            Node = Node.next
        self.min = None
        for degree in range(int (math.log(self.n,2)) + 1):
            if DegreeArray[degree] != None:
                if self.min == None:
                    self.rootList = DoubleLoopLinkListSentinel()
                    self.rootList.Insert(DegreeArray[degree])
                    self.min = DegreeArray[degree]
                else:
                    self.rootList.Insert(DegreeArray[degree])
                    if self.min.key > DegreeArray[degree].key:
                        self.min = DegreeArray[degree]
    def __HeapLink(self,LargeNode,LittleNode):
        self.rootList.Delete(LargeNode)
        LargeNode.parent =  LittleNode
        if LittleNode.key.child != None:
            LittleNode.key.child.Insert(LargeNode)
        else:
            LittleNode.key.child = DoubleLoopLinkListSentinel()
            LittleNode.key.child.Insert(LargeNode)
        
        LittleNode.key.degree  = LittleNode.key.degree + 1
        LargeNode.mark = False  #
    def PrettyPrint(self,FibNodeList,NumTab):
        if FibNodeList != None:
            Node = FibNodeList.nil.next 
            while Node != FibNodeList.nil:
                print '----' * NumTab + str(Node.key.key)
                self.PrettyPrint(Node.key.child,NumTab + 1)
                Node = Node.next
if __name__ == '__main__':
    FibHeapob = FibHeap(comparetor)
    
    for i in range(10):
        FibHeapob.Insert(FibHeapNode(i))
    FibHeapob.ExtractMin()
    FibHeapob.PrettyPrint(FibHeapob.rootList,0)
    
    
    
            
        
    
        
        
                
            
            
        