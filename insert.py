import bst
from bst import Node

def insert(tree, key):
  node = Node(key)
  node.color = 'red'
  tree = bst.insert(tree, node)
  insert_case_1(tree, node)
  return tree

def insert_case_1(tree, node):
  # print('insert_case_1', tree.key, node.key)
  parent = bst.get_parent(tree, node.key)
  if parent is None:
    node.color='black'
    return
  else:
    insert_case_2(tree, node, parent)

def insert_case_2(tree, node, parent):
  # print('insert_case_2', tree.key, node.key, parent.key)
  if parent.color=='black':
    return
  else:
    insert_case_3(tree, node, parent)

def insert_case_3(tree, node, parent):
  # print('insert_case_3', tree.key, node.key, parent.key)
  grand_parent = bst.get_parent(tree, parent.key)
  uncle = bst.get_uncle(tree, parent.key)
  if uncle is not None and uncle.color=='red':
    parent.color='black'
    uncle.color='black'
    grand_parent.color='red'
    insert_case_1(tree, grand_parent)
  else:
    insert_case_4(tree, node, parent, grand_parent)

def insert_case_4(tree, node, parent, grand_parent):
  # print('insert_case_4', tree.key, node.key, parent.key, grand_parent.key)
  if node==parent.left and parent==grand_parent.left:
    print('rotate_right(grand_parent)')
    node = node.left
  else:
    print('rotate_left(grand_parent)')
    node = node.right
  insert_case_5(tree, node)
    
def insert_case_5(tree, node): # TODO: not work
  parent = bst.get_parent(tree, node)
  grand_parent = bst.get_parent(tree, parent)
  parent.color = 'black'
  grand_parent.color = 'red'

  if node==parent.left:
    print('rotate_right(grand_parent)')
  else:
    print('rotate_left(grand_parent)')


def make_tree(keys): # return Node
    tree = None
    for idx, key in enumerate(keys):
      print(idx, key)
      if idx==0:
        tree = insert(tree, key)
      else:
        insert(tree, key)
      
    return tree

tree = make_tree([30, 20, 25, 40, 10, 35, 66, 33, 1, 2, 5, 19, 20])
tree.display()
