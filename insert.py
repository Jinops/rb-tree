import bst
from bst import Node

def insert(tree, key):
  node = Node(key)
  node.color = 'red'
  tree = bst.insert(tree, node)
  insert_case_1(tree, node)

def insert_case_1(tree, node):
  #print('insert_case_1', node.key)
  parent = bst.get_parent(tree, node.key)
  if parent is None:
    node.color='black'
    return
  else:
    insert_case_2(tree, node, parent)

def insert_case_2(tree, node, parent):
  #print('insert_case_2', node.key, parent.key)
  if parent.color=='black':
    return
  else:
    insert_case_3(tree, node, parent)

def insert_case_3(tree, node, parent):
  #print('insert_case_3', node.key, parent.key)
  grand_parent = bst.get_parent(tree, parent.key)
  uncle=None
  if grand_parent.left == parent:
    uncle = grand_parent.right
  else:
    uncle = grand_parent.left
  if uncle is not None and uncle.color=='red':
    parent.color='black'
    uncle.color='black'
    grand_parent.color='red'
    insert_case_1(tree, grand_parent)
  else:
    insert_case_4(tree, node, parent, grand_parent)

def insert_case_4(tree, node, parent, grand_parent):
  #print('insert_case_4', node.key, parent.key, grand_parent.key)
  if node==parent.left and parent==grand_parent.left:
    print('rotate_right')
  else:
    print('rotate_left')

tree = bst.make_tree([30, 20, 25, 40, 10, 35])
insert(tree, 55)
tree.display()
insert(tree, 3)
tree.display()
insert(tree, 30)
tree.display()
insert(tree, 40)
tree.display()
insert(tree, 50)
tree.display()
insert(tree, 60)
tree.display()