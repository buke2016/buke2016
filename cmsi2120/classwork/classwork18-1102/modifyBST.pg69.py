#xracted from Data_structures_the_fun_way_page 69 (95 OF 307)
RemoveTreeNode(BinarySearchTree: tree, TreeNode: node):
    if tree.root == null OR node == null: # step 1
        return
    # Case A: Deleting a leaf node.
    if node.left == null AND node.right == null: #step 2
        if node.parent == null:
            tree.root = null
        elif node.parent.left == node:
            node.parent.left = null
        else:
            node.parent.right = null
        return
    # Case B: Deleting a node with one child.
    if node.left == null OR node.right == null: # step 3
       TreeNode: child = node.left  #step 4
        if node.left == null:
            child = node.right
        child.parent = node.parent #step 5
        if node.parent == null:
            tree.root = child
        elif node.parent.left == node:
            node.parent.left = child
        elif:
            node.parent.right = child
        return
    # Case C: Deleting a node with two children.
    # Find the successor and splice it out of the tree.
    TreeNode: successor = node.right #step 6
    while successor.left != null:
        successor = successor.left
    RemoveTreeNode(tree, successor)
    # Insert the successor in the deleted node's place.
    if node.parent == null: #step 7
        tree.root = successor
    elif node.parent.left == node:
        node.parent.left = successor
    else:
        node.parent.right = successor
    successor.parent = node.parent #step 8
    successor.left = node.left #step 9
    node.left.parent = successor
    successor.right = node.right
    if node.right != null:
        node.right.parent = successor