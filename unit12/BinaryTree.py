#coding:utf-8
import copy
class BinaryTreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key
    
class BinaryTree:
    def __init__(self):
        self.Root = None
    def InorderTreeWalk(self,Tree):
        if Tree != None:
            self.InorderTreeWalk(Tree.left)
            print Tree.key,
            self.InorderTreeWalk(Tree.right)
    
    def TreeSearch(self,k,Node):
        while Node != None and k != Node.key:
            if k < Node.key:
                Node = Node.left
            else:
                Node = Node.right
        return Node
        
    def TreeMax(self,Node):
        while Node.right != None:
            Node = Node.right
        return Node
    def TreeMin(self,Node):
        while Node.left != None:
            Node = Node.left
        return Node
    
    def TreeSuccessor(self,Node):
        if Node.right != None:
            return self.TreeMin(Node.right)
            
        NodeParent = Node.p
        while NodeParent != None and NodeParent.right == Node:
            Node = NodeParent
            NodeParent = NodeParent.p
        return NodeParent
        
    def TreeInsert(self,key):
        NodeParent = None
        InsertNode = BinaryTreeNode(key)
        Node = self.Root
        
        while Node != None:
            NodeParent = Node
            if key < Node.key:
                Node = Node.left
            else:
                Node = Node.right
        
        InsertNode.p = NodeParent  #当树为空时,NodeParent = None,作为判断树根的条件Node.p == None
        if NodeParent == None:
            self.Root = InsertNode
        elif InsertNode.key < NodeParent.key:
            NodeParent.left = InsertNode
        else:
            NodeParent.right = InsertNode
    def Transplant(self,oldNode,newNode):
        if oldNode.p == None:
            self.Root = newNode
        elif oldNode.p.left == oldNode:
            oldNode.p.left = newNode
        else:
            oldNode.p.right = newNode
        if newNode != None:
            newNode.p = oldNode.p
    def TreeDelete(self,DeleteNode):
        if DeleteNode.left == None:
            self.Transplant(DeleteNode,DeleteNode.right)
        elif DeleteNode.right == None:
            self.Transplant(DeleteNode,DeleteNode.left)
        else:
            MinNode = self.TreeMin(DeleteNode.right)
            if MinNode.p != DeleteNode:#当右子树的最小元素的双亲节点不是被删除的节点
                self.Transplant(MinNode,MinNode.right)
                MinNode.right = DeleteNode.right
                MinNode.right.p = MinNode
            
            #将右子树中最小的元素当做根，然后将被删除的左子树当做新的左子树，改变根的左子树和左子树的双亲
            self.Transplant(DeleteNode,MinNode)
            MinNode.left = DeleteNode.left
            MinNode.left.p = MinNode
            
            
        
        
BinaryTreeob = BinaryTree()
array = [15,6,18,3,7,17,20,2,4,13,9  ]
for i in range(len(array)):
    BinaryTreeob.TreeInsert(array[i])


print "二叉树最小值:",
MinNode = BinaryTreeob.TreeMin(BinaryTreeob.Root)
print MinNode.key
print "二叉树最大值:",
MaxNode = BinaryTreeob.TreeMax(BinaryTreeob.Root)
print MaxNode.key
print 
print "最小节点的后继:",
print BinaryTreeob.TreeSuccessor(MinNode).key
BinaryTreeob.TreeDelete(BinaryTreeob.Root)
print "二叉树中序遍历:",
BinaryTreeob.InorderTreeWalk(BinaryTreeob.Root)
            
            
        
        
        
        
    