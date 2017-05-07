class RBTreeNode:
    def __init__(self,key = None,color = None):
        self.key = key
        self.color = color
        self.p = None
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(None,"Black")
        self.Root = self.nil
    def LeftRotate(self,Node):
        RightSon = Node.right
        Node.Right = RightSon.left
        if RightSon.left != self.nil:
            RightSon.left.p = Node
        RightSon.p = Node.p
        if Node.p == self.nil:
            self.Root = RightSon
        elif Node == Node.p.left:
            Node.p.left = RightSon
        else:
            Node.p.right = RightSon
        RightSon.left = Node
        Node.p = RightSon
    def RightRotate(self,Node):
        LeftSon = Node.left
        Node.left = LeftSon.right
        if LeftSon.right != self.nil:
            LeftSon.right.p = Node
        LeftSon.p = Node.p
        if Node.p == self.nil:
            self.Root = LeftSon
        elif Node == Node.p.left:
            Node.p.left = LeftSon
        else:
            Node.p.right = LeftSon
        LeftSon.Right = Node
        Node.p = LeftSon
    def RBInsert(self,Node):
        ParentNode = self.nil
        x = self.Root
        while x != self.nil:
            ParentNode = x
            if Node.key < x.key:
                x = x.left
            else:
                x = x.right
        Node.p = ParentNode
        if ParentNode == self.nil:
            self.Root = Node
        elif Node.key < ParentNode.key:
            ParentNode.left = Node
        else:
            ParentNode.right = Node
        Node.left = self.nil
        Node.right = self.nil
        Node.color = "Red"
        self.RB_InsertFixUp(Node)
    def RB_InsertFixUp(Node):
        while Node.p.color == "Red":
            if Node.p == Node.p.p.left:
                UncleNode = Node.p.p.right
                if UncleNode == "Red":
                    Node.p.color= "Black"
                    Uncle.color = "Black"
                    Node.p.p.color = "Red"
                    Node = Node.p.p
                elif Node == Node.p.right:
                    Node = Node.p
                    self.LeftRotate(Node)
                Node.p.color = "Black"
                Node.p.p.color = "Red"
                self.RightRotate(Node.p.p)
            else:
                UncleNode = Node.p.p.left
                if UncleNode == "Red":
                    Node.p.color = "Black"
                    Uncle.color = "Black"
                    Node.p.p.color = "Red"
                    Node = Node.p.p
                elif Node == Node.p.left:
                    Node = Node.p
                    self.RightRotate(Node)
                Node.p.color = "Black"
                Node.p.p.color = "Red"
                self.LeftRotate(Node.p.p)
        self.Root.color = "Black"
    
