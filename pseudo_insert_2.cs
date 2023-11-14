def insert(tree, key):
  node.color='red'
  node.left=NIL
  node.right=NIL

  tree.bst_insert(node)
  insert_case_1(node)

def insert_case_1(node):
  if node=root:
    node.color='black'
    return
  else:
    insert_case_2(node)

def insert_case_2(node):
  parent=node.parent
  if parent.color='black':
    return
  else:
    insert_case_3(node)

def insert_case_3(node):
  parent=node.parent
  uncle=node.uncle
  if uncle.color='red':
    parent='black'
    uncle='black'
    parent.parent='red'
  else:
    insert_case_4(node)

def insert_case_4(node):
  parent=node.parent
  grand_parent=parent.parent
  if node=parent.left and parent=grand_parent.left:
    rotate_right(grand_parent)
  else:
    rotate_left(grand_parent)
