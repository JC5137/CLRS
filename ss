[1mdiff --git a/unit13/RBTree.py b/unit13/RBTree.py[m
[1mindex b0697bc..70e596c 100644[m
[1m--- a/unit13/RBTree.py[m
[1m+++ b/unit13/RBTree.py[m
[36m@@ -2,16 +2,17 @@[m
 import random[m
 import copy[m
 class RBTreeNode:[m
[31m-    def __init__(self,key = None,color = None):[m
[32m+[m[32m    def __init__(self,key = None,color = None,size = 1):[m
         self.key = key[m
         self.color = color[m
         self.p = None[m
         self.left = None[m
         self.right = None[m
[32m+[m[32m        self.size = size[m
 [m
 class RBTree:[m
     def __init__(self):[m
[31m-        self.Nil = RBTreeNode(None,"Black")[m
[32m+[m[32m        self.Nil = RBTreeNode(None,"Black",0)[m
         self.Root = self.Root.p = self.Nil[m
     def TreeMin(self,Node):[m
         MinNode = Node[m
[36m@@ -21,8 +22,26 @@[m [mclass RBTree:[m
     def OrderPrintTree(self,Tree,i):[m
         if Tree != self.Nil:[m
             self.OrderPrintTree(Tree.left,i+1)[m
[31m-            print '\t' * i + str(Tree.key) + ":"  + Tree.color[m
[32m+[m[32m            print '\t' * i + str(Tree.key) + ":"  + Tree.color + ":" + str(Tree.size)[m
             self.OrderPrintTree(Tree.right,i+1)[m
[32m+[m[32m    def Select(self,Tree,i):[m
[32m+[m[32m        rank = Tree.left.size + 1[m
[32m+[m[32m        if i == rank:[m
[32m+[m[32m            return Tree[m
[32m+[m[32m        elif i < rank:[m
[32m+[m[32m            return self.Select(Tree.left,i)[m
[32m+[m[32m        else:[m
[32m+[m[32m            return self.Select(Tree.right,i - rank)[m
[32m+[m[32m    def Rank(self,Node):[m
[32m+[m[32m        rank = Node.left.size + 1[m
[32m+[m[41m        [m
[32m+[m[32m        NodeTemp = Node[m
[32m+[m[32m        while NodeTemp != self.Root:[m
[32m+[m[32m            if NodeTemp.p.right == NodeTemp:[m
[32m+[m[32m                rank = rank + NodeTemp.p.left.size + 1[m
[32m+[m[32m            NodeTemp = NodeTemp.p[m
[32m+[m[32m        return rank[m
[32m+[m[41m        [m
             [m
     def LeftRotate(self,Node):[m
         RightSon = Node.right           #将Node右子树的左子树作为Node的新的右子树[m
[36m@@ -38,6 +57,10 @@[m [mclass RBTree:[m
             Node.p.right = RightSon[m
         RightSon.left = Node           #用Node作为其右子树的左节点，完成拼接[m
         Node.p = RightSon[m
[32m+[m[41m        [m
[32m+[m[32m        RightSon.size = Node.size[m
[32m+[m[32m        Node.size = Node.left.size + Node.right.size + 1[m
[32m+[m[41m        [m
     def RightRotate(self,Node):[m
         LeftSon = Node.left            #用Node的左子树的右孩子作为Node的左子树[m
         Node.left = LeftSon.right[m
[36m@@ -54,11 +77,16 @@[m [mclass RBTree:[m
         [m
         LeftSon.right = Node         #用Node作为其左子树的右节点，完成拼接[m
         Node.p = LeftSon[m
[32m+[m[32m        LeftSon.size = Node.size[m
[32m+[m[32m        Node.size = Node.left.size + Node.right.size + 1[m
[32m+[m[41m        [m
[32m+[m[41m        [m
         [m
     def RB_Insert(self,Node):[m
         ParentNode = self.Nil[m
         x = self.Root[m
         while x != self.Nil:[m
[32m+[m[32m            x.size = x.size + 1          #沿着路径size +　１[m
             ParentNode = x[m
             if Node.key < x.key:[m
                 x = x.left[m
[36m@@ -114,19 +142,29 @@[m [mclass RBTree:[m
             OldNode.p.left = NewNode[m
         else:[m
             OldNode.p.right = NewNode[m
[32m+[m[32m        NewNode.size = OldNode.size[m
         NewNode.p = OldNode.p[m
[32m+[m[32m    def ReSizeFromNodeToRoot(self,Node):[m
[32m+[m[32m        ParentNode = Node.p[m[41m [m
[32m+[m[32m        while ParentNode != self.Nil:[m[41m [m
[32m+[m[32m            ParentNode.size = ParentNode.size - 1[m
[32m+[m[32m            ParentNode = ParentNode.p[m
[32m+[m[41m        [m
     def RB_Delete(self,Node):[m
         y = Node  [m
         yOrginalColor = y.color[m
         if Node.left == self.Nil:[m
             x = Node.right[m
[32m+[m[32m            self.ReSizeFromNodeToRoot(y)[m
             self.RB_TransPlant(Node,Node.right)[m
         elif Node.right == self.Nil:[m
             x = Node.left[m
[32m+[m[32m            self.ReSizeFromNodeToRoot(y)[m
             self.RB_TransPlant(Node,Node.left)[m
         else:[m
             y = self.TreeMin(Node.right)[m
             yOrginalColor = y.color[m
[32m+[m[32m            self.ReSizeFromNodeToRoot(y)[m
             x = y.right[m
             if y.p == Node:[m
                 x.p = y[m
[36m@@ -138,7 +176,7 @@[m [mclass RBTree:[m
             y.left = Node.left[m
             y.left.p = y[m
             y.color = Node.color[m
[31m-            [m
[32m+[m[41m        [m
         if yOrginalColor == "Black":[m
             self.RB_DeleteFixUp(x)[m
     def RB_DeleteFixUp(self,Node):[m
[36m@@ -190,21 +228,28 @@[m [mclass RBTree:[m
         Node.color = "Black"[m
                 [m
 RBTreeob = RBTree()[m
[31m-TreeNode = [0] * 100[m
[32m+[m[32mlist = [26,17,41,14,21,30,47,10,16,19,21,28,38,7,12,14,20,35,39,3][m
[32m+[m[32mTreeNode = [0] * len(list)[m
 [m
[31m-[m
[31m-for i in range(100):[m
[31m-    TreeNode[i] = RBTreeNode(random.randint(1,100))[m
[32m+[m[32mfor i in range(len(list)):[m
[32m+[m[32m    TreeNode[i] = RBTreeNode(list[i])[m
     RBTreeob.RB_Insert(TreeNode[i])[m
 [m
 [m
[32m+[m[32m# for i in range(100):[m
[32m+[m[32m    # TreeNode[i] = RBTreeNode(random.randint(1,100))[m
[32m+[m[32m    # RBTreeob.RB_Insert(TreeNode[i])[m
[32m+[m
[32m+[m
 [m
[31m-for i in range(50):[m
[31m-    RBTreeob.RB_Delete(TreeNode[i])[m
[32m+[m[32m# for i in range(50):[m
[32m+[m[32m    # RBTreeob.RB_Delete(TreeNode[i])[m
     [m
 [m
 [m
 [m
[31m-RBTreeob.OrderPrintTree(RBTreeob.Root,0)[m
[32m+[m[32m#RBTreeob.OrderPrintTree(RBTreeob.Root,0)[m
[32m+[m[32m#print RBTreeob.Select(RBTreeob.Root,17).key[m
[32m+[m[32mprint RBTreeob.Rank(TreeNode[12])[m
 [m
 [m
