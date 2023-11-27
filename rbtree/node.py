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
  def _display_aux_key(self):
     if self.color=='red':
      return 'r%sr' % self.key
     else:
      return 'b%sb' % self.key
  ####
