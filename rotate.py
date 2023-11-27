from rbtree_base import *

class RBTreeRotate(RBTreeBase):
  def rotate_left(self, node):
    child = node.right
    parent = node.parent

    if child.left is not None:
      child.left.parent = node

    node.right = child.left
    node.parent = child
    child.left = node
    child.parent = parent

    if parent is not None:
      if parent.left == node:
        parent.left = child
      else:
        parent.right = child
    else:
      self.root = child

  def rotate_right(self, node):
    child = node.left
    parent = node.parent

    if child.right is not None:
      child.right.parent = node

    node.left = child.right
    node.parent = child
    child.right = node
    child.parent = parent

    if parent is not None:
      if parent.right == node:
        parent.right = child
      else:
        parent.left = child
    else:
      self.root = child
