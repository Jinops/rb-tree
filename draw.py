import graphviz

def draw(root):
    dot = graphviz.Digraph()

    if root is not None:
        dot.node(str(root.key), color=root.color)

        def add_nodes_edges(node):
            if node.left:
                dot.node(str(node.left.key), color=node.left.color)
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.key), color=node.right.color)
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right)
        add_nodes_edges(root)

    dot.render('data/tree', view=False, format='png')
