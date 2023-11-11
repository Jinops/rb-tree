from bst import *

def insert(tree, key):
  node를 초기화하고, red로 설정한다.
  node의 양 쪽 자식을 NIL로 설정한다.
  트리에 node를 삽입한다. # BST

  insert_case_1(node)로 전체 검증을 시작한다.

def insert_case_1(node): 
  # node가 루트라면, black으로 설정한 뒤 종료한다.
  if node가 루트라면:
    black으로 설정한 뒤 종료한다.
  else:
    insert_case_2(node) 검증을 시행한다.

def insert_case_2(node): 
  # 부모의 색을 확인한다.
  if 부모가 black이라면:
    종료한다.
  else:
    insert_case_3(node) 검증을 시행한다.

def insert_case_3(node): 
  # 부모가 red인 경우, 삼촌의 색을 확인한다.
  if 삼촌이 red라면:
    부모와 삼촌(부모의 형제)를 black으로 설정한다.
    조부모(부모의 부모)를 red로 설정한다.
    insert_case_1(조부모) 검증을 시행한다.
  else:
    insert_case_4(node) 검증을 시행한다.

def insert_case_4(node): 
  # 부모는 red, 삼촌은 black인 경우, rotate를 한다.
  if node가 부모의 왼쪽 자식이고, 부모는 조부모의 오른쪽 지식이면:
    rotate_right(부모)를 시행한다.
    node의 역할을 오른쪽 자식이 대신한다. # node=n.right
  else if node가 부모의 오른쪽 자식이고, 부모는 조부모의 왼쪽 자식이면:
    rotate_left(부모)를 시행한다.
    node의 역할을 왼쪽 자식이 대신한다. # node=n.left
  
  insert_case_5(node) 검증을 시행한다.

def insert_case_5(node): 
  # 부모가 조부모의 어느 쪽 자식인지에 따라 rotate를 한다.
  부모를 black, 조부모를 red로 설정한다.
  if node가 부모의 왼쪽 자식이면:
    rotate_right(조부모)를 시행한다.
  else:
    rotate_left(조부모)를 시행한다.
