#coding:utf-8
import random
class BNode:
    def __init__(self,KeyNum = None,IsLeaf = None,Keys = None,ChildPointers = None):
        self.KeyNum = KeyNum
        self.IsLeaf = IsLeaf
        self.Keys =           [ None for i in range(KeyNum) ]
        self.ChildPointers = [ None for i in range(KeyNum + 1) ]
class BTree:
    def __init__(self):
        self.Root = None
        self.BTreeCreate()
        self.T = 2
    def BTreeCreate(self):
        Node = BNode(0,True)
        self.Root = Node
        #Disk_Write(Node)
        
    def BTreeSearch(self,Node,Key):
        i = 0
        while i < Node.KeyNum and Key > Node.Keys[i]:
            i = i + 1
        if i < Node.KeyNum and Key == Node.Keys[i]:
            return (Node,i)
        elif Node.IsLeaf == True:
            return None
        else:
            #Disk_Read(Node,Node.ChildPointers[i])
            return self.BTreeSearch(Node.ChildPointers[i],Key)
    #Index is MidKeys Indexed in ParentNode
    def BTreeSplitChild(self,Node,Index):
        SplitedNode = Node.ChildPointers[Index] #获取待分隔节点
        NewNode = BNode(self.T - 1,SplitedNode.IsLeaf) #从待分隔节点分隔出的新的节点
        
        
        for j in range(0,NewNode.KeyNum):#新的节点数据的填充
            NewNode.Keys[j] = SplitedNode.Keys[j + self.T]

        if SplitedNode.IsLeaf == False:
            for j in range(0,NewNode.KeyNum + 1):#新的节点孩子节点的填充
                NewNode.ChildPointers[j] = SplitedNode.ChildPointers[j + self.T]
        SplitedNode.KeyNum = self.T - 1
        
        Node.ChildPointers.append(None)
        for j in range(Index + 1,Node.KeyNum + 1)[::-1]:#所有节点的孩子节点向后移动一个位置，空出Index + 1的位置，对新的节点进行连接
            Node.ChildPointers[j + 1] = Node.ChildPointers[j]
        Node.ChildPointers[Index + 1] = NewNode
        
        Node.Keys.append(None)
        for j in range(Index,Node.KeyNum)[::-1]:#所有节点的关键字向后移动一个位置，空出Index位置，将带分隔节点的T - 1填入 
            Node.Keys[j + 1] = Node.Keys[j]
        Node.Keys[Index] = SplitedNode.Keys[self.T - 1]
        
        Node.KeyNum = Node.KeyNum + 1
        #DISK_Write(SplitedNode)
        #DISK_Write(NewNode)
        #Disk_Write(Node)
    def BTreeInsertNonFull(self,Node,Key):
        Index = Node.KeyNum - 1
        
        if Node.IsLeaf == True:
            Node.Keys.append(None)
            Node.ChildPointers.append(None)
            while Index >= 0 and Key < Node.Keys[Index]:
                Node.Keys[Index + 1]  = Node.Keys[Index]
                Index = Index - 1
            Node.Keys[Index + 1] = Key
            Node.KeyNum = Node.KeyNum + 1
            #DiskWrite(Node)
        else:
            while Index >= 0 and Key < Node.Keys[Index]: 
                Index = Index - 1
            Index = Index + 1 #从后往前,找到关键词分割点的位置
            
            #DiskRead(Node.ChildPointers[Index])
            if Node.ChildPointers[Index].KeyNum == 2 * self.T - 1:
                self.BTreeSplitChild(Node,Index)
                if Key > Node.Keys[Index]: #如果大于新的分割点，向后移动一个单位
                    Index = Index + 1
            self.BTreeInsertNonFull(Node.ChildPointers[Index],Key)
    def BTreeInsert(self,Key):
        _root = self.Root
        if _root.KeyNum == 2 * self.T - 1:
            NewNode = BNode(0,False)
            self.Root = NewNode
            NewNode.ChildPointers[0] = _root
            self.BTreeSplitChild(NewNode,0)
            self.BTreeInsertNonFull(NewNode,Key)
        else:
            self.BTreeInsertNonFull(_root,Key)
    def PrintBTree(self,Node,TabNum):
        print '----' * TabNum,
        print Node.Keys[0:Node.KeyNum]
        if Node.IsLeaf != True:
            for i in range(Node.KeyNum + 1):
                self.PrintBTree(Node.ChildPointers[i],TabNum + 1)
        
            
            

       
if __name__ == "__main__":
    BTreeobj = BTree()
    List = ['M','D','H','Q','T','X','B','C','F','G','J','K','L','N','P','R','S','V','W','Y','Z',27,48,1,5,7,10,40,25,17,24]
    for i in range(len(List)):
        BTreeobj.BTreeInsert(List[i])
    BTreeobj.PrintBTree(BTreeobj.Root,0)
    # print BTreeobj.BTreeSearch(BTreeobj.Root,'F')
    # for i in range(2048):
        # BTreeobj.BTreeInsert(random.randint(0,1000))
    # BTreeobj.PrintBTree(BTreeobj.Root,0)
    
        
    
    
    
          
            
            
            
            
            
        
