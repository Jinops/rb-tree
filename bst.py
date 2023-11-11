# alternative of https://github.com/Jinops/ie-algo/blob/main/4_BST.ipynb
class Node():
  def __init__(self, key, color=None):
    self.key = key
    self.left = None    
    self.right = None
    self.color = color # 'red' | 'black'

def insert(node, x, color=None): # return Node
    if node is None: 
        return Node(x, color)
    if x < node.key: 
        node.left = insert(node.left, x, color)
    else:
        node.right = insert(node.right, x, color)
    return node

def search(node, x): # return Node
  return _search_with_parent(node, x)[0]
  
def get_parent(node, x): # return Node
  return _search_with_parent(node, x)[1]

def delete(node, key): # return Node
  target_node, parent_node = _search_with_parent(node, key)    
  if target_node == node: 
    node = _delete_node(target_node)
  elif target_node == parent_node.left:
    parent_node.left = _delete_node(target_node)
  elif target_node == parent_node.right:
    parent_node.right = _delete_node(target_node)
  return node

def get_uncle(node, x): # return Node
  parent = get_parent(node, x)
  grand_parent = get_parent(node, parent.key)
  if grand_parent is not None:
    if grand_parent.left is parent:
      return grand_parent.right
    if grand_parent.right is parent:
      return grand_parent.left
  return None

def _search_with_parent(node, x, parent=None): # private / return (Node, Node)
  if node is None or node.key == x: 
    return node, parent
  if x < node.key: 
    return _search_with_parent(node.left, x, node)
  else:
    return _search_with_parent(node.right, x, node)
    
def _delete_node(node): # private / return Node
  if node.left is None and node.right is None: 
    return None
  if node.left is None: 
    return node.right
  if node.right is None: 
    return node.left
  else: 
    s = node.right 
    while s.left is not None: 
      s_parent = s
      s = s.left
    node.key = s.key 
    if node.right == s: 
      node.right = s.right 
    elif s.right is not None: 
      s_parent.left = s.right
    return node

def make_tree(keys): # return Node
    tree = None
    for key in keys:
        tree = insert(tree, key)
    return tree

def print_tree(t): # void
  import queue
  if t == None:
    return
  Q = queue.Queue()
  Q.put(t)
  while not Q.empty():
    u = Q.get()
    print(u.key, end=" - ")
    if u.left != None:
      Q.put(u.left)
      print(u.left.key, end="")
    print("", end=" - ")
    if u.right != None:
      Q.put(u.right)
      print(u.right.key, end="")
    print()

def _test(): # example code for Test
  keys = [30, 20, 25, 40, 10, 35]
  tree = make_tree(keys)
  tree = insert(tree, 55)
  tree = delete(tree, 30)
  node = search(tree, 55)
  parent = get_parent(tree, 55)
  uncle = get_uncle(tree, 55)
  print_tree(tree)
  print("%d's parent is %d" %(node.key, parent.key))
  print("%d's uncle is %d" %(node.key, uncle.key))

# _test()
