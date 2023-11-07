class TreeNode:
    def __init__(self, val):
      self.val = val
      self.children = []
    def findvalueItr(self, root, target):
      current = self.root
      while current != null AND current.value != target:
        if current < current.value:
          current = current.left
        else:
          current = current.right
      return current

    def findValueRec(current, target):
      if current == null:
        return null
      if current.val == target:
        return current
      if current < current.val AND current.left !=null:
        return findValueRec(current.left, target)
      if target > current.value AND current.right != null:
        return findValueRec(current.right, target)
      return null