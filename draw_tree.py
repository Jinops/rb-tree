import graphviz
import image_manager

is_nil_visibile=False
def draw(tree):
    graph_attr={'nodesep': '0.3', 'ranksep': '0.3'}
    graph = graphviz.Digraph(graph_attr=graph_attr)

    def add_node(node):
        if tree.focused == node:
            graph.node(str(node.key), color=node.color, width='0.3', height='0.4', fillcolor='#FEF9E7', style='filled')
            tree.focused == None
        else:
            graph.node(str(node.key), color=node.color, width='0.3', height='0.4')

    def add_nodes_edges(node):
        if node.left:
            add_node(node.left)
            graph.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            add_node(node.right)
            graph.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)
        if is_nil_visibile and (node.left is None and node.right is None):
            graph.node(f'nil_{node.key}', 'nil', shape='box', width='0.2', height='0.3',\
                     fillcolor='black', fontcolor='white',style='filled')
            graph.edge(str(node.key), f'nil_{node.key}')


    if tree.root is not None:
        add_node(tree.root)
        add_nodes_edges(tree.root)

    graph.render(image_manager.new_path(), view=False, format=image_manager.format, cleanup=True)
