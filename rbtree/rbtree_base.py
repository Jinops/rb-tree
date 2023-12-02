from node import Node

import os, sys; 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class RBTreeBase:
  def __init__(self):
     self.root = None
     self.focused = None
  
  def display(self):
    if self.root is not None:
      self.root.display()

  def search(self, key):
    self.focused = self._search_recur(self.root, key)
    return self.focused

  def _search_recur(self, node, key):
    if node is None or node.key == key: 
      return node
    if key < node.key: 
      return self._search_recur(node.left, key)
    else:
      return self._search_recur(node.right, key)


    
