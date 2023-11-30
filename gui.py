import sys
import rbtree.rbtree as rbtree
import draw
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QCheckBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from functools import partial

class MyApp(QWidget):
  def __init__(self, tree):
      super().__init__()
      self.tree = rbtree.RBTree() if tree is None else tree
      self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)
    self.setWindowTitle('Red-black Tree')
    self.setGeometry(300, 300, 300, 200)
    self.setFixedSize(700, 560)

    label_num = QLabel('Input a number below:')
    btn_insert = QPushButton('&Insert', self)
    btn_delete = QPushButton('&Delete', self)
    btn_search = QPushButton('&Search', self)
    btn_reset = QPushButton('&Reset', self)
    btn_sample = QPushButton('&Sample', self)
    checkbox_nil = QCheckBox('Show nil', self)
    self.label_status = QLabel('Ready')
    self.edit_num = QLineEdit()
    self.img_label = QLabel('tree')
    
    self.update_image_label()
    self.img_label.setFixedSize(500, 500)
    self.img_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.img_label.setStyleSheet("background-color: white")

    self.label_status.setAlignment(Qt.AlignCenter)

    checkbox_nil.setStyleSheet("margin-left:10%; margin-bottom:10%")

    btn_insert.clicked.connect(partial(self.onclick, 'insert'))
    btn_delete.clicked.connect(partial(self.onclick, 'delete'))
    btn_search.clicked.connect(partial(self.onclick, 'search'))

    btn_reset.clicked.connect(self.reset)
    btn_sample.clicked.connect(self.generate_sample)
    checkbox_nil.stateChanged.connect(self.on_checkbox_change)

    grid.addWidget(label_num, 0, 0)
    grid.addWidget(self.edit_num, 1, 0)
    grid.addWidget(btn_insert, 2, 0)
    grid.addWidget(btn_delete, 3, 0)
    grid.addWidget(btn_search, 4, 0)
    grid.addWidget(QLabel("<hr/>"), 5, 0)
    grid.addWidget(btn_reset, 6, 0)
    grid.addWidget(btn_sample, 7, 0)
    grid.addWidget(QLabel("<hr/>"), 9, 0)
    grid.addWidget(self.label_status, 10, 0)
    grid.addWidget(checkbox_nil, 28, 1)
    grid.addWidget(self.img_label, 0, 1, 30, 1)
    checkbox_nil.raise_()
    self.show()

    print(self.size())

  def onclick(self, value):
    num = self.edit_num.text()
    if not num.isdecimal():
       self.label_status.setText('Input number first!')
       return
    
    num = int(num)
    if value == 'insert':
      self.tree.insert(num)
    elif value == 'delete':
      node = self.tree.search(num)
      if node is None:
       self.label_status.setText(f'{num} not found')
       return
      self.tree.delete(node)
    elif value == 'search':
      node = self.tree.search(num)
      if node is None:
       self.label_status.setText(f'{num} not found')
       return
    else:
       return
    self.update_image_label()
    self.label_status.setText(f'{value}: {num}')
    self.edit_num.clear()

  def update_image_label(self):
    draw.draw(self.tree)
    self.img_label.setPixmap(QPixmap('data/tree.png'))

  def reset(self):
    if self.confirm('reset') == QMessageBox.Yes:
      del self.tree
      self.tree = rbtree.RBTree()
      self.update_image_label()
      self.label_status.setText('reset')
  
  def generate_sample(self):
    if self.confirm('make sample tree') == QMessageBox.Yes:
      del self.tree
      self.tree = get_sample_tree()
      self.update_image_label()
      self.label_status.setText('sample generated')

  def confirm(self, job=''):
    return QMessageBox.question(self, 'Confirmation', f'Do you really want to {job}?',\
                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

  def on_checkbox_change(self, state):
    draw.is_nil_visibile = state == Qt.Checked
    self.update_image_label()

def run(tree):
  app = QApplication(sys.argv)
  ex = MyApp(tree)
  sys.exit(app.exec_())

def get_sample_tree():
    keys = [30, 20, 25, 40, 10, 35, 22, 13]
    return rbtree.generate(keys)


if __name__ == "__main__":
    tree = get_sample_tree()
    # tree = None
    run(tree)
