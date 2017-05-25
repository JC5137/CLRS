class BNode:
    def __init__(self,KeyNum = None,IsLeaf = None,Keys = None,ChildPointers = None):
        self.KeyNum = KeyNum
        self.IsLeaf = IsLeaf
        self.Keys =           [ None for i in range(KeyNum) ]
        self.ChinldPointers = [ None for i in range(KeyNum + 1) ]
class BTree:
    def __init__(self):
        self.Root = None
        self.BTreeCreate()
        self.T = 4
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
        NewNode = BNode()
        SplitedNode = Index.ChildPointers[Index]
        NewNode.IsLeaf = SplitedNode.IsLeaf
        NewNode.KeyNum = self.T - 1
        for j in range(0,NewNode.KeyNum):
            NewNode.Keys[j] = SplitedNode[j + self.T + 1]
        if SplitNode.IsLeaf == False:
            for j in range(0,NewNode.KeyNum + 1):
                NewNode.ChildPointers[j] = SplitedNode.ChildPointers[j + self.T + 1]
        SplitedNode.KeyNum = t - 1
        
        Node.ChildPointers.append(None)
        for j in range(index + 1,Node.KeyNum + 1)[::-1]:
            Node.ChildPointers[j + 1] = Node.ChildPointers[j]
        Node.ChildPointers[Index + 1] = NewNode
        
        Node.Keys.append(None)
        for j in range(Index,Node.KeyNum)[::-1]:
            Node.keys[j + 1] = Node.ChildPointers[j]
        Node.keys[Index] = SplitedNode.keys[self.T - 1]
        
        Node.KeyNum = Node.KeyNum + 1
        #DISK_Write(SplitedNode)
        #DISK_Write(NewNode)
        #Disk_Write(Node)
    def BTreeInsert(self,Key):
        _root = self.Root
        if _root.KeyNum == 2 * self.T - 1:
            NewNode = BNode(0,False)
            self.root = NewNode
            NewNode.ChildPointers[0] = _root
            self.BTreeSplitChild(NewNode,0)
            self.BTreeInsertNonFull(NewNode,Key)
        else:
            self.BTreeInsertNonFull(_root,Key)
            
    def BTreeInsertNonFull(self,Node,Key):
        Index = Node.KeyNum - 1
        
        if Node.IsLeaf == True:
            Node.Keys.append(None)
            while Index >= 0 and Key < Node.Keys[Index]:
                Node.Keys[Index + 1]  = Node.Keys[Index]
                Index = Index - 1
            Node.Keys[Index + 1] = Key
            Node.KeyNum = Node.KeyNum + 1
            #DiskWrite(Node)
        else:
            while Index >= 0 and Key < Node.Keys[Index]:
                Index = Index - 1
            Index = Index +　1
            #DiskRead(Node.ChildPointers[Index])
            if Node.ChildPointers[Index].KeyNum = 2 * self.T - 1:
                self.BTreeSplitChild(Node,Index)
                if Key > Node.Keys[Index]:
                    Index = Index + 1
            self.BTreeInsertNonFull(Node.ChildPointers[Index],Key)
        
        
            
            
            
            
            
        
