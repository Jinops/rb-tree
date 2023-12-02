import sys
import rbtree.rbtree as rbtree
import draw_tree
import file_manager
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QToolButton, QLabel, QMessageBox, QCheckBox, QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from functools import partial

class MyApp(QWidget):
  def __init__(self, tree):
      super().__init__()
      self.tree = rbtree.RBTree() if tree is None else tree
      self.img_width=600
      self.img_height=550
      self.img_idx=0
      self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)
    self.setWindowTitle('Red-black Tree')
    self.setGeometry(300, 300, 300, 200)
    self.setFixedSize(800, 600)

    label_num = QLabel('Node')
    btn_insert = QPushButton('&Insert', self)
    btn_delete = QPushButton('&Delete', self)
    btn_search = QPushButton('&Search', self)
    label_controller = QLabel('History') # Include rotating
    controller = QHBoxLayout()
    btn_prev = QPushButton('&<', self)
    btn_next = QPushButton('&>', self)
    btn_last = QPushButton('&Last Step')
    label_utility = QLabel('Utility')
    btn_reset = QPushButton('&Reset', self)
    btn_sample = QPushButton('&Sample', self)
    checkbox_nil = QCheckBox('Show nil')
    self.label_status = QLabel('Ready')
    self.edit_num = QLineEdit()
    self.img_label = QLabel('tree')
    
    self.update_tree_image()
    self.img_label.setFixedSize(self.img_width, self.img_height)
    self.img_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.img_label.setStyleSheet("background-color: white")

    self.label_status.setAlignment(Qt.AlignCenter)

    checkbox_nil.setStyleSheet("margin-left:10%; margin-bottom:10%")

    btn_prev.setStyleSheet("background-color:white; width:50%;")
    btn_next.setStyleSheet("background-color:white; width:50%;")

    btn_insert.clicked.connect(partial(self.onclick, 'insert'))
    btn_delete.clicked.connect(partial(self.onclick, 'delete'))
    btn_search.clicked.connect(partial(self.onclick, 'search'))

    btn_prev.clicked.connect(self.prev_image)
    btn_next.clicked.connect(self.next_image)
    btn_last.clicked.connect(partial(self.update_image_pixmap, None))

    btn_reset.clicked.connect(self.reset)
    btn_sample.clicked.connect(self.generate_sample)
    checkbox_nil.stateChanged.connect(self.on_checkbox_change)

    controller.addWidget(btn_prev)
    controller.addWidget(btn_next)

    grid.addWidget(label_num, 0, 0)
    grid.addWidget(self.edit_num, 1, 0)
    grid.addWidget(btn_insert, 2, 0)
    grid.addWidget(btn_delete, 3, 0)
    grid.addWidget(btn_search, 4, 0)
    grid.addWidget(QLabel("<hr/>"), 5, 0)
    grid.addWidget(label_controller, 6, 0)
    grid.addLayout(controller, 7, 0)
    grid.addWidget(btn_last, 8, 0)
    grid.addWidget(QLabel("<hr/>"), 9, 0)
    grid.addWidget(label_utility, 10, 0)
    grid.addWidget(btn_reset, 11, 0)
    grid.addWidget(btn_sample, 12, 0)
    grid.addWidget(QLabel("<hr/>"), 13, 0)
    grid.addWidget(self.label_status, 14, 0)
    grid.addWidget(checkbox_nil, 28, 1)
    grid.addWidget(self.img_label, 0, 1, 30, 1)
    checkbox_nil.raise_()
    self.show()

  def onclick(self, value):
    num = self.edit_num.text()
    if not num.isdecimal():
       self.label_status.setText('Input number first!')
       return
    
    num = int(num)
    if value == 'insert':
      node = self.tree.insert(num)
      if node is None:
        self.label_status.setText(f'{num} is Duplicated')
        self.update_tree_image()
        return
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
    self.update_tree_image()
    self.label_status.setText(f'{value}: {num}')
    self.edit_num.clear()

  def update_tree_image(self):
    draw_tree.draw(self.tree)
    self.update_image_pixmap()
  
  def update_image_pixmap(self, idx=None):
    if idx is not None:
      pixmap = QPixmap(file_manager.path(idx))
      self.img_idx=idx
    else:
      pixmap = QPixmap(file_manager.last_path())
      self.img_idx=file_manager.last_idx
    if pixmap.width() > self.img_width*1.1 or pixmap.height() > self.img_height*1.1:
      pixmap = pixmap.scaled(int(self.img_width*1.1), int(self.img_height*1.1), Qt.KeepAspectRatio)
    pixmap.scaled(500, 500, Qt.KeepAspectRatio)
    self.img_label.setPixmap(pixmap)

  def prev_image(self):
    if self.img_idx>0:
      self.update_image_pixmap(self.img_idx-1)

  def next_image(self):
    if self.img_idx<file_manager.last_idx:
      self.update_image_pixmap(self.img_idx+1)
  
  def reset(self):
    if self.confirm('reset') == QMessageBox.Yes:
      del self.tree
      file_manager.clear()
      self.tree = rbtree.RBTree()
      self.update_tree_image()
      self.label_status.setText('reset')
  
  def generate_sample(self):
    if self.confirm('make sample tree') == QMessageBox.Yes:
      del self.tree
      self.tree = get_sample_tree()
      self.update_tree_image()
      self.label_status.setText('sample generated')

  def confirm(self, job=''):
    return QMessageBox.question(self, 'Confirmation', f'Do you really want to {job}?',\
                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

  def on_checkbox_change(self, state):
    draw_tree.is_nil_visibile = state == Qt.Checked
    self.update_tree_image()

def run(tree):
  app = QApplication(sys.argv)
  ex = MyApp(tree)
  sys.exit(app.exec_())

def get_sample_tree():
    keys = [30, 20, 25, 40, 10, 35, 22, 13]
    return rbtree.generate(keys)


if __name__ == "__main__":
    tree = get_sample_tree()
    run(tree)
