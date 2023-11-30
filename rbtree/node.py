class Node():
  def __init__(self, key, parent, color='red'):
    self.key = key
    self.left = None    
    self.right = None
    self.parent = parent
    self.color = color # 'red' | 'black'

  def get_uncle(self): # return Node
    parent = self.parent
    grand_parent = self.parent.parent
    if grand_parent is not None:
      if grand_parent.left is parent:
        return grand_parent.right
      if grand_parent.right is parent:
        return grand_parent.left
    return None
