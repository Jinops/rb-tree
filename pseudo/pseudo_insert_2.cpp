insert(tree, key){
  node.color <- 'red';
  node.left <- NIL;
  node.right <- NIL;

  tree.bst_insert(node);
  insert_case_1(node);
}

bst_insert(tree, node){
  if (tree=NULL) then return node
  if (node.key < tree.key)
  then tree.left = bst_insert(tree.left, node)
  else tree.right = bst_insert(tree.right, node)
}

insert_case_1(node){
  if (node=root) then node.color='black'; return;
  else insert_case_2(node);
}

insert_case_2(node){
  parent <- node.parent;
  if (parent.color='black') then return;
  else insert_case_3(node);
}

insert_case_3(node){
  parent <- node.parent;
  grand_parent <- parent.parent;
  if (grand_parent.left=parent)
  then uncle <- grand_parent.right;
  else uncle <- grand_parent.left;
  if (uncle.color='red')
  then {
    parent.color <- 'black';
    uncle.color <- 'black';
    grand_parent.color <-'red';
    insert_case_1(grand_parent)
  }
  else insert_case_4(node);
}

insert_case_4(node){
  parent <- node.parent;
  grand_parent <- parent.parent;
  if (node=parent.right and parent=grand_parent.left)
  then rotate_left(grand_parent); node <- node.left;
  else if (node=parent.left and parent=grand_parent.right)
  then rotate_right(grand_parent); node <- node.right;
  insert_case_5(node);
}

insert_case_5(node){
  parent <- node.parent;
  grand_parent <- parent.parent;
  parent.color <- 'black';
  grand_parent.color <- 'red';
  if (node=parent.left)
  then rotate_right(grand_parent);
  else rotate_left(grand_parent);
}
