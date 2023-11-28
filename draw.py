import graphviz

def draw(tree):
    dot = graphviz.Digraph()

    def add_node(node):
        if tree.focused == node:
            dot.node(str(node.key), color=node.color, fillcolor='#FEF9E7', style='filled')
            tree.focused == None
        else:
            dot.node(str(node.key), color=node.color)

    def add_nodes_edges(node):
        if node.left:
            add_node(node.left)
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            add_node(node.right)
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    if tree.root is not None:
        add_node(tree.root)
        add_nodes_edges(tree.root)

    dot.render('data/tree', view=False, format='png')
