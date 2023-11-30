from insert import *
from delete import *

class RBTree(RBTreeInsert, RBTreeDelete):
  pass

def generate(keys):
    tree = RBTree()
    for key in keys:
        tree.insert(key)
    return tree
