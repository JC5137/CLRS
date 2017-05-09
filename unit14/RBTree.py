#coding:utf-8
import random
import copy
class RBTreeNode:
    def __init__(self,key = None,color = None,size = 1):
        self.key = key
        self.color = color
        self.p = None
        self.left = None
        self.right = None
        self.size = size

class RBTree:
    def __init__(self):
        self.Nil = RBTreeNode(None,"Black",0)
        self.Root = self.Root.p = self.Nil
    def TreeMin(self,Node):
        MinNode = Node
        while MinNode.left != self.Nil:
            MinNode = MinNode.left
        return MinNode
    def OrderPrintTree(self,Tree,i):
        if Tree != self.Nil:
            self.OrderPrintTree(Tree.left,i+1)
            print '\t' * i + str(Tree.key) + ":"  + Tree.color + ":" + str(Tree.size)
            self.OrderPrintTree(Tree.right,i+1)
    def Select(self,Tree,i):
        rank = Tree.left.size + 1
        if i == rank:
            return Tree
        elif i < rank:
            return self.Select(Tree.left,i)
        else:
            return self.Select(Tree.right,i - rank)
    def Rank(self,Node):
        rank = Node.left.size + 1
        
        NodeTemp = Node
        while NodeTemp != self.Root:
            if NodeTemp.p.right == NodeTemp:
                rank = rank + NodeTemp.p.left.size + 1
            NodeTemp = NodeTemp.p
        return rank
        
            
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
        
        RightSon.size = Node.size
        Node.size = Node.left.size + Node.right.size + 1
        
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
        LeftSon.size = Node.size
        Node.size = Node.left.size + Node.right.size + 1
        
        
        
    def RB_Insert(self,Node):
        ParentNode = self.Nil
        x = self.Root
        while x != self.Nil:
            x.size = x.size + 1          #沿着路径size +　１
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
        NewNode.size = OldNode.size
        NewNode.p = OldNode.p
    def ReSizeFromNodeToRoot(self,Node):
        ParentNode = Node.p 
        while ParentNode != self.Nil: 
            ParentNode.size = ParentNode.size - 1
            ParentNode = ParentNode.p
        
    def RB_Delete(self,Node):
        y = Node  
        yOrginalColor = y.color
        if Node.left == self.Nil:
            x = Node.right
            self.ReSizeFromNodeToRoot(y)
            self.RB_TransPlant(Node,Node.right)
        elif Node.right == self.Nil:
            x = Node.left
            self.ReSizeFromNodeToRoot(y)
            self.RB_TransPlant(Node,Node.left)
        else:
            y = self.TreeMin(Node.right)
            yOrginalColor = y.color
            self.ReSizeFromNodeToRoot(y)
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
                
RBTreeob = RBTree()
list = [26,17,41,14,21,30,47,10,16,19,21,28,38,7,12,14,20,35,39,3]
TreeNode = [0] * len(list)

for i in range(len(list)):
    TreeNode[i] = RBTreeNode(list[i])
    RBTreeob.RB_Insert(TreeNode[i])


# for i in range(100):
    # TreeNode[i] = RBTreeNode(random.randint(1,100))
    # RBTreeob.RB_Insert(TreeNode[i])



# for i in range(50):
    # RBTreeob.RB_Delete(TreeNode[i])
    



RBTreeob.OrderPrintTree(RBTreeob.Root,0)
print RBTreeob.Select(RBTreeob.Root,17).key
print RBTreeob.Rank(TreeNode[12])


