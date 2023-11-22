import sys
import insert
from draw import draw
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from functools import partial

class MyApp(QWidget):
  def __init__(self, node):
      super().__init__()
      self.node = node
      self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)
    self.setWindowTitle('Red-black Tree')
    self.setGeometry(300, 300, 300, 200)

    label_num = QLabel('Input a number below:')
    self.label_status = QLabel('Ready')
    self.edit_num = QLineEdit()
    btn_insert = QPushButton('&Insert', self)
    btn_delete = QPushButton('&Delete', self)
    btn_search = QPushButton('&Search', self)
    self.img_label = QLabel('tree')

    self.update_image_label()
    self.img_label.setFixedSize(500, 500)
    self.img_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.img_label.setStyleSheet("background-color: white")

    self.label_status.setAlignment(Qt.AlignCenter)

    btn_insert.clicked.connect(partial(self.onclick, 'insert'))
    btn_delete.clicked.connect(partial(self.onclick, 'delete'))
    btn_search.clicked.connect(partial(self.onclick, 'search'))

    grid.addWidget(label_num, 0, 0)
    grid.addWidget(self.edit_num, 1, 0)
    grid.addWidget(btn_insert, 2, 0)
    grid.addWidget(btn_delete, 3, 0)
    grid.addWidget(btn_search, 4, 0)
    grid.addWidget(QLabel("<hr/>"), 5, 0)
    grid.addWidget(self.label_status, 6, 0)
    grid.addWidget(self.img_label, 0, 1, 30, 1)
    self.show()

  def onclick(self, value):
    num = self.edit_num.text()
    if not num.isdecimal():
       self.label_status.setText('Input number first!')
       return
    
    num = int(num)
    if value == 'insert':
      if self.node == None:
        self.node = insert.insert(self.node, num)
      else:
         insert.insert(self.node, num)
    elif value == 'delete':
       pass # TODO
    elif value == 'search':
       pass # TODO
    else:
       return
    self.update_image_label()
    self.label_status.setText('{}: {}'.format(value, num))
    self.edit_num.clear()

  def update_image_label(self):
    draw(self.node)
    self.img_label.setPixmap(QPixmap('tree.png'))

def run(node):
  app = QApplication(sys.argv)
  ex = MyApp(node)
  sys.exit(app.exec_())
  gui.run(tree)

if __name__ == "__main__":
    keys = [30, 20, 25, 40, 10, 35, 22, 13]
    run(insert.make_tree(keys))
