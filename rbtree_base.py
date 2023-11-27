from node import Node

class RBTreeBase:
  def __init__(self):
     self.root = None
  
  def display(self):
    if self.root is not None:
      self.root.display()

  def search(self, key):
    return self._search_recur(self.root, key)

  def _search_recur(self, node, key):
    if node is None or node.key == key: 
      return node
    if key < node.key: 
      return self._search_recur(node.left, key)
    else:
      return self._search_recur(node.right, key)
  

    
