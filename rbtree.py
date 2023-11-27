from insert import *
from delete import *

class RBTree(RBTreeInsert, RBTreeDelete):
  pass

def make_tree(keys): # return Node
    tree = RBTree()
    for key in keys:
        tree.insert(key)
    return tree
  
if __name__ == "__main__":
  keys = [1, 10, 13]
  tree = make_tree(keys)
  #tree.display()