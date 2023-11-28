from rotate import *

class RBTreeInsert(RBTreeRotate):
  def insert(self, key):
    print('<insert>', key)
    node = self._bst_insert(key)
    self.focused = node
    if node is None:
      return
    if self.root is None:
       self.root = node
    self._insert_case_1(node)
    # self.display()

  def _bst_insert(self, key):
    return self._bst_insert_recur(self.root, key)[1]

  def _bst_insert_recur(self, node, key, parent=None): # return [node for recursive, new node]
      if node is None: 
        new_node = Node(key, parent, 'red')
        return new_node, new_node
      if node.key == key:
          print(f"Duplicated key: {node.key}")
          return node, None
      if key < node.key: 
          node.left, new_node = self._bst_insert_recur(node.left, key, node)
      else:
          node.right, new_node = self._bst_insert_recur(node.right, key, node)
      return node, new_node
  
  def _insert_case_1(self, node):
    # self.display()
    print('_insert_case_1', node.key)
    if node.parent is None:
      node.color='black'
      return
    else:
      self._insert_case_2(node)

  def _insert_case_2(self, node):
    # self.display()
    print('_insert_case_2', node.key)
    if node.parent.color=='black':
      return
    else:
      self._insert_case_3(node)

  def _insert_case_3(self, node):
    # self.display()
    print('_insert_case_3', node.key)
    uncle = node.get_uncle()
    grand_parent =  node.parent.parent
    if uncle is not None and uncle.color=='red':
      node.parent.color='black'
      uncle.color='black'
      grand_parent.color='red'
      self._insert_case_1(grand_parent)
    else:
      self._insert_case_4(node)

  def _insert_case_4(self, node):
    # self.display()
    grand_parent = node.parent.parent
    print('_insert_case_4', node.key)
    if node==node.parent.right and node.parent==grand_parent.left:
      print('rotate_left')
      self.rotate_left(node.parent)
      node = node.left
    elif node==node.parent.left and node.parent==grand_parent.right:
      print('rotate_right')
      self.rotate_right(node.parent)
      node = node.right
      
    self._insert_case_5(node)
      
  def _insert_case_5(self, node):
    # self.display()
    print('_insert_case_5', node.key)
    parent = node.parent
    grand_parent = parent.parent
    parent.color = 'black'
    grand_parent.color = 'red'

    if node==parent.left:
      print('rotate_right(g)')
      self.rotate_right(grand_parent)
    else:
      print('rotate_left(g)')
      self.rotate_left(grand_parent)
