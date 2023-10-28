class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Tree:
    def __init__(self):
        self.root: TreeNode = None

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

class BinaryTree:
    def __init__(self):
        root: BinaryTreeNode = None

    def preorderPrint(self, n: BinaryTreeNode):

        if n == None:
            return

        print(n.val)
        self.preorderPrint(n.left)
        self.preorderPrint(n.right)

    def postorderPrint(self, n: BinaryTreeNode):

        if n == None:
            return

        self.postorderPrint(n.left)
        self.postorderPrintorderPrint(n.right)
        print(n.val)

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

class BinarySearchTree:
    def __init__(self):
        root: BinaryTreeNode = None

    def addValue(self, val):
        ...

my_tree = Tree()

my_tree.root = TreeNode(2)
my_tree.children[0] = TreeNode(3)