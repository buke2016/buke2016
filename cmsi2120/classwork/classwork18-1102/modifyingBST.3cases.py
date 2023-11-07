def RemoveTreeNode(tree, node):
  if tree.root is None or node is None:
    return

  # Case A: Deleting a leaf node.
  if node.left is None and node.right is None:
    if node.parent is None:
      tree.root = None
    elif node.parent.left == node:
      node.parent.left = None
    else:
      node.parent.right = None
    return

  # Case B: Deleting a node with one child.
  if node.left is None or node.right is None:
    child = node.left
    if node.left is None:
      child = node.right

    child.parent = node.parent
    if node.parent is None:
      tree.root = child
    elif node.parent.left == node:
      node.parent.left = child
    else:
      node.parent.right = child
    return

  # Case C: Deleting a node with two children.
  successor = node.right
  while successor.left is not None:
    successor = successor.left

  RemoveTreeNode(tree, successor)

  if node.parent is None:
    tree.root = successor
  elif node.parent.left == node:
    node.parent.left = successor
  else:
    node.parent.right = successor

  successor.parent = node.parent
  successor.left = node.left
  node.left.parent = successor
  successor.right = node.right
  if node.right is not None:
    node.right.parent = successor
