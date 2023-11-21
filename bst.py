# alternative of https://github.com/Jinops/ie-algo/blob/main/4_BST.ipynb
class Node():
  def __init__(self, key, color='red'):
    self.key = key
    self.left = None    
    self.right = None
    self.color = color # 'red' | 'black'

  ## NOT MY CODE ##
  def display(self):
      lines, *_ = self._display_aux()
      for line in lines:
          print(line)
  def _display_aux(self):
      """Returns list of strings, width, height, and horizontal coordinate of the root."""
      # No child.
      if self.right is None and self.left is None:
          line = self._display_aux_key()
          width = len(line)
          height = 1
          middle = width // 2
          return [line], width, height, middle

      # Only left child.
      if self.right is None:
          lines, n, p, x = self.left._display_aux()
          s = self._display_aux_key()
          u = len(s)
          first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
          second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
          shifted_lines = [line + u * ' ' for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

      # Only right child.
      if self.left is None:
          lines, n, p, x = self.right._display_aux()
          s = self._display_aux_key()
          u = len(s)
          first_line = s + x * '_' + (n - x) * ' '
          second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
          shifted_lines = [u * ' ' + line for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

      # Two children.
      left, n, p, x = self.left._display_aux()
      right, m, q, y = self.right._display_aux()
      s = self._display_aux_key()
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
      second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
      if p < q:
          left += [n * ' '] * (q - p)
      elif q < p:
          right += [m * ' '] * (p - q)
      zipped_lines = zip(left, right)
      lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
      return lines, n + m + u, max(p, q) + 2, n + u // 2
  ####
  def _display_aux_key(self):
     if self.color=='red':
      return '*%s*' % self.key
     else:
      return '>%s<' % self.key

def insert(tree, node): # return Node
    if tree is None: 
        return node
    if node.key == tree.key:
        print(f"Duplicated key: {node.key}")
        return tree
    if node.key < tree.key: 
        tree.left = insert(tree.left, node)
    else:
        tree.right = insert(tree.right, node)
    return tree

def search(tree, x): # return Node
  return _search_with_parent(tree, x)[0]
  
def get_parent(tree, x): # return Node
  return _search_with_parent(tree, x)[1]

def delete(node, key): # return Node
  target_node, parent_node = _search_with_parent(node, key)    
  if target_node == node: 
    node = _delete_node(target_node)
  elif target_node == parent_node.left:
    parent_node.left = _delete_node(target_node)
  elif target_node == parent_node.right:
    parent_node.right = _delete_node(target_node)
  return node

def get_uncle(tree, x): # return Node
  parent = get_parent(tree, x)
  grand_parent = get_parent(tree, parent.key)
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
    for idx, key in enumerate(keys):
        if idx==0:
          tree = insert(tree, Node(key))
        else:
          insert(tree, Node(key))
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
  insert(tree, Node(55))
  delete(tree, 30)
  node = search(tree, 55)
  parent = get_parent(tree, 55)
  uncle = get_uncle(tree, 55)
  print_tree(tree)
  print("%d's parent is %d" %(node.key, parent.key))
  print("%d's uncle is %d" %(node.key, uncle.key))

# _test()
