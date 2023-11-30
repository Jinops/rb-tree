# author: Jihyeon Kim

from rotate import *

class RBTreeDelete(RBTreeRotate):
  def delete(self, node):
    if node != None:
      self.delete_node(node)

  def delete_node(self, node):
    y = node
    y_color = y.color
    if node.left is None:
      x = node.right
      self.transplant(node, node.right)
    elif node.right is None:
      x = node.left
      self.transplant(node, node.left)
    else:
      y = self.minimum(node.right)
      y_color = y.color
      x = y.right
      if y.parent != node:
        self.transplant(y, y.right)
        y.right = node.right
        y.right.parent = y
      self.transplant(node, y)
      y.left = node.left
      y.left.parent = y
      y.color = node.color

    if y_color == 'black':
      self.delete_fixup(x)


  def delete_fixup(self, x):
    if x is None:
      return
    while x != self.root and x.color == 'black':
      if x == x.parent.left:
        sibling = x.parent.right

        if sibling is not None and sibling.color == 'red':
          sibling.color = 'black'
          x.parent.color = 'red'
          self.rotate_left(x.parent)
          sibling = x.parent.right

        if sibling is not None:
          if (sibling.left is None or sibling.left.color == 'black') \
          and (sibling.right is None or sibling.right.color == 'black'):
            sibling.color = 'red'
            x = x.parent
          else:
            if sibling.right is None or sibling.right.color == 'black':
              if sibling.left is not None:
                sibling.left.color = 'black'
              sibling.color = 'red'
              self.rotate_right(sibling)
              sibling = x.parent.right

            sibling.color = x.parent.color
            x.parent.color = 'black'
            if sibling.right is not None:
              sibling.right.color = 'black'
            self.rotate_left(x.parent)
            x = self.root
        else:
          break
      else:
        sibling = x.parent.left

        if sibling is not None and sibling.color == 'red':
          sibling.color = 'black'
          x.parent.color = 'red'
          self.rotate_right(x.parent)
          sibling = x.parent.left

        if sibling is not None:
          if (sibling.right is None or sibling.right.color == 'black') \
            and (sibling.left is None or sibling.left.color == 'black'):
            sibling.color = 'red'
            x = x.parent
          else:
            if sibling.left is None or sibling.left.color == 'black':
              if sibling.right is not None:
                sibling.right.color = 'black'
              sibling.color = 'red'
              self.rotate_left(sibling)
              sibling = x.parent.left

            sibling.color = x.parent.color
            x.parent.color = 'black'
            if sibling.left is not None:
              sibling.left.color = 'black'
            self.rotate_right(x.parent)
            x = self.root
        else:
          break

    if x is not None:
      x.color = 'black'


  def transplant(self, u, v):
    if u.parent is None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    if v is not None:
      v.parent = u.parent

  def minimum(self, x):
    while x.left != None:
      x = x.left
    return x