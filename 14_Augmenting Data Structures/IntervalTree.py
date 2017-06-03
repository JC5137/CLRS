#coding:utf-8
import random
import copy
class IntervalTreeNode:
    def __init__(self,key = None,color = None,interval = None):
        self.key = key
        self.color = color
        self.p = None
        self.left = None
        self.right = None
        self.interval = interval
        self.max = max(interval)

class IntervalTree:
    def __init__(self):
        self.Nil = IntervalTreeNode(None,"Black",(-float('inf'),-float('inf')))
        self.Root = self.Root.p = self.Nil
    def TreeMin(self,Node):
        MinNode = Node
        while MinNode.left != self.Nil:
            MinNode = MinNode.left
        return MinNode
    def OrderPrintTree(self,Tree,i):
        if Tree != self.Nil:
            self.OrderPrintTree(Tree.left,i+1)
            print '\t' * i + str(Tree.interval) + "-" + str(Tree.max) + ":"  + Tree.color
            self.OrderPrintTree(Tree.right,i+1)
    def IntervalSearch(self,TimeNode):
        IsIntervalOverlap = lambda x,y: True if x[0] <= y[1] and y[0] <= x[1] else False
        x = self.Root
        while x != self.Nil and not IsIntervalOverlap(TimeNode,x.interval):
            if x.left != self.Nil and x.left.max >= TimeNode[0]:
                x = x.left
            else:
                x = x.right
        return x
            
    def LeftRotate(self,Node):
        RightSon = Node.right           #将Node右子树的左子树作为Node的新的右子树
        Node.right = RightSon.left
        if RightSon.left != self.Nil:   
            RightSon.left.p = Node
        RightSon.p = Node.p             #用Node的右子树代替Node，进行Node父节点的拼接
        if Node.p == self.Nil:
            self.Root = RightSon
        elif Node == Node.p.left:
            Node.p.left = RightSon
        else:
            Node.p.right = RightSon
        RightSon.left = Node           #用Node作为其右子树的左节点，完成拼接
        Node.p = RightSon
        RightSon.max = max(RightSon.interval[1],RightSon.left.max,RightSon.right.max) #更新最大区间，选择原始区间最大值与子树的区间最大值比较
    def RightRotate(self,Node):
        LeftSon = Node.left            #用Node的左子树的右孩子作为Node的左子树
        Node.left = LeftSon.right
        if LeftSon.right != self.Nil:
            LeftSon.right.p = Node
        
        LeftSon.p = Node.p            #用Node的左子树代替Node，进行Node父节点的拼接
        if Node.p == self.Nil:
            self.Root = LeftSon
        elif Node == Node.p.left:
            Node.p.left = LeftSon
        else:
            Node.p.right = LeftSon
        
        LeftSon.right = Node         #用Node作为其左子树的右节点，完成拼接
        Node.p = LeftSon
        LeftSon.max = max(LeftSon.interval[1],LeftSon.left.max,LeftSon.right.max) #更新最大区间，选择原始区间最大值与子树的区间最大值比较
    def UpdateNodeMax(self,Node):
        ParentNode = Node.p
        while ParentNode != self.Nil:
            ParentNode.max = max(ParentNode.interval[1],ParentNode.left.max,ParentNode.right.max)
            ParentNode = ParentNode.p
    def RB_Insert(self,Node):
        ParentNode = self.Nil
        x = self.Root
        while x != self.Nil:
            ParentNode = x
            if Node.key < x.key:
                x = x.left
            else:
                x = x.right
        Node.p = ParentNode
        if ParentNode == self.Nil:
            self.Root = Node
        elif Node.key < ParentNode.key:
            ParentNode.left = Node
        else:
            ParentNode.right = Node
        Node.left = self.Nil
        Node.right = self.Nil
        Node.color = "Red"
        self.UpdateNodeMax(Node)  #顺子节点向上更新其父节点的max值
        self.RB_InsertFixUp(Node)
        
    def RB_InsertFixUp(self,Node):
        while Node.p.color == "Red" :
            if Node.p == Node.p.p.left:        #父亲节点为爷爷节点的左节点
                UncleNode = Node.p.p.right     #叔叔节点为爷爷节点的右节点
                if UncleNode.color == "Red":   #第一种情况 叔节点为红色
                    Node.p.color= "Black"
                    UncleNode.color = "Black"
                    Node.p.p.color = "Red"
                    Node = Node.p.p
                elif Node == Node.p.right:     #第二种情况 叔节点为黑色,且Node为父节点的右节点
                    Node = Node.p
                    self.LeftRotate(Node)
                else:
                    Node.p.color = "Black"     #第三种情况 叔节点为黑色,且Node为父节点的左节点
                    Node.p.p.color = "Red" 
                    self.RightRotate(Node.p.p)
            else:                              #对称情况，left与right互换
                UncleNode = Node.p.p.left
                if UncleNode.color == "Red":   #第一种情况 叔节点为红色
                    Node.p.color = "Black"
                    UncleNode.color = "Black"
                    Node.p.p.color = "Red"
                    Node = Node.p.p
                elif Node == Node.p.left:      #第二种情况 叔节点为黑色,且Node为父节点的左节点
                    Node = Node.p
                    self.RightRotate(Node)
                else:
                    Node.p.color = "Black"     #第三种情况 叔节点为黑色,且Node为父节点的右节点
                    Node.p.p.color = "Red"
                    self.LeftRotate(Node.p.p)
        self.Root.color = "Black"
        
    def RB_TransPlant(self,OldNode,NewNode):
        if OldNode.p == self.Nil:
            self.Root = NewNode
        elif OldNode == OldNode.p.left:
            OldNode.p.left = NewNode
        else:
            OldNode.p.right = NewNode
        NewNode.p = OldNode.p
    def RB_Delete(self,Node):
        y = Node  
        yOrginalColor = y.color
        if Node.left == self.Nil:
            x = Node.right
            self.RB_TransPlant(Node,Node.right)
        elif Node.right == self.Nil:
            x = Node.left
            self.RB_TransPlant(Node,Node.left)
        else:
            y = self.TreeMin(Node.right)
            yOrginalColor = y.color
            x = y.right
            if y.p == Node:
                x.p = y
            else:
                self.RB_TransPlant(y,y.right)
                y.right = Node.right
                y.right.p = y
            self.RB_TransPlant(Node,y)
            y.left = Node.left
            y.left.p = y
            y.color = Node.color
        
        self.UpdateNodeMax(x)    
        if yOrginalColor == "Black":
            self.RB_DeleteFixUp(x)
    def RB_DeleteFixUp(self,Node):
        while Node != self.Root and Node.color == "Black":
            if Node == Node.p.left:
                BrotherNode = Node.p.right
                if BrotherNode.color == "Red":
                    BrotherNode.color = "Black"
                    Node.p.color = "Red"
                    self.LeftRotate(Node.p)
                    BrotherNode = Node.p.right
                if BrotherNode.left.color == "Black" and BrotherNode.right.color == "Black":
                    BrotherNode.color = "Red"
                    Node = Node.p
                elif BrotherNode.right.color == "Black":
                    BrotherNode.left.color = "Black"
                    BrotherNode.color = "Red"
                    self.RightRotate(BrotherNode)
                    BrotherNode = Node.p.right
                else:                                       #
                    BrotherNode.color = Node.p.color
                    Node.p.color = "Black"
                    BrotherNode.right.color = "Black"
                    self.LeftRotate(Node.p)
                    
                    Node = self.Root
            else:
                BrotherNode = Node.p.left
                if BrotherNode.color == "Red":
                    BrotherNode.color = "Black"
                    Node.p.color = "Red"
                    self.RightRotate(Node.p)
                    BrotherNode = Node.p.left
                if BrotherNode.left.color == "Black" and BrotherNode.right.color == "Black":
                    BrotherNode.color = "Red"
                    Node = Node.p
                elif BrotherNode.left.color == "Black":
                    BrotherNode.right.color = "Black"
                    BrotherNode.color = "Red"
                    self.LeftRotate(BrotherNode)
                    BrotherNode = Node.p.left
                else:    
                    BrotherNode.color = Node.p.color
                    Node.p.color = "Black"
                    BrotherNode.left.color = "Black"
                    self.RightRotate(Node.p)
                    
                    Node = self.Root
        Node.color = "Black"
                
IntervalTreeob = IntervalTree()
list = [ (16,21),(8,9),(25,30),(5,8),(15,23),(17,19),(26,26),(0,3),(6,10),(19,20) ]

TreeNode = [0] * len(list)


for i in range(len(list)):
    TreeNode[i] = IntervalTreeNode(list[i][0],None,list[i])
    IntervalTreeob.RB_Insert(TreeNode[i])



#IntervalTreeob.RB_Delete(TreeNode[8])

    



IntervalTreeob.OrderPrintTree(IntervalTreeob.Root,0)
print u"查找(22,25)的重叠区间: ",
print IntervalTreeob.IntervalSearch((22,25)).interval

