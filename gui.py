import sys
from PyQt5.QtWidgets import (QApplication, QStatusBar, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from functools import partial

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
    grid = QGridLayout()
    self.setLayout(grid)
    # self.statusBar().showMessage('Ready')
    self.setWindowTitle('Red-black Tree')
    self.setGeometry(300, 300, 300, 200)

    label_num = QLabel('Input a number below:')
    self.label_status = QLabel('Ready')
    self.edit_num = QLineEdit()
    btn_insert = QPushButton('&Insert', self)
    btn_delete = QPushButton('&Delete', self)
    btn_search = QPushButton('&Search', self)
    img_label_tree = QLabel('')
    img_label_tree.setPixmap(QPixmap('tree.png'))
    # self.label_status.setAlignment(Qt.AlignCenter)

    btn_insert.clicked.connect(partial(self.onclick, 'insert'))
    btn_delete.clicked.connect(partial(self.onclick, 'delete'))
    btn_search.clicked.connect(partial(self.onclick, 'search'))

    grid.addWidget(label_num, 0, 0)
    grid.addWidget(self.edit_num, 1, 0)
    grid.addWidget(btn_insert, 2, 0)
    grid.addWidget(btn_delete, 3, 0)
    grid.addWidget(btn_search, 4, 0)
    grid.addWidget(img_label_tree, 0, 1, 30, 5)
    grid.addWidget(self.label_status, 31, 0, 1, 5)
    self.show()

  def onclick(self, value):
    num = self.edit_num.text()
    if not num.isdecimal():
       self.label_status.setText('Input number first!')
       return
    self.label_status.setText('{}: {}'.format(value, num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())