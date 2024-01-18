# red-black-tree
Red-black Tree Visualization in python

![gui](./resources/screenshot.png)

## Installation
1. Install Libraries
```
pip install PyQt5
```
```
pip install graphviz
```
2. Install Graphviz

(Windows)

2.1. Download [Graphviz 2.38](https://www2.graphviz.org/Archive/stable/windows/graphviz-2.38.msi) and install it. You need to copy paths of installed directories.

2.2. Add PATH system variable `[Your Graphviz Path]\bin` 
(ex. `C:\Program Files (x86)\Graphviz2.38\bin`).

> **위 설치과정 및 환경변수 설정이 반드시 필요합니다.**


3. run main.py
```
python3 main.py
```

##  Description

### rbtree
The main code of the Red-black Tree is modularized as 'rbtree'. Within the 'rbtree' module, all classes have hierarchical relationship.

Red-black Tree 구현부는, rbtree로 모듈화되어 있습니다.
해당 모듈에는 주요 기능(rotate, insert, delete)들 간의 상속관계가 있으며, 최종적으로 RBTree 클래스를 사용합니다.

```
RBTreeBase
└── RBTreeRotate
    ├── RBTreeInsert ┐
    └── RBTreeDelete ┴ RBTree
```

### gui

Code for Graphic User Interfaces, Initialized by main.py.

UI를 만드는 코드로, main.py에 의해 실행됩니다. PyQt5 라이브러리를 사용합니다.

### draw_tree

Generate images from Tree.

rbtree class로부터, 이미지를 생성합니다. 

### file_manager

Save, load, and manage temporary folders.

이미지를 저장할 임시 폴더를 생성 및 삭제하고, 파일명을 관리합니다.
