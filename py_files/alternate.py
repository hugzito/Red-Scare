import networkx as nx

def alternate(graph, a, b):
    try: shortest_path = nx.shortest_path(graph, a, b)
    except:return False
    return True

def assign_weights_alternate(graph):
    nodes = nx.get_node_attributes(graph, 'color')
    for k, j in list(graph.edges()):
        if nodes[j] == 'red' and nodes[k] == 'teal':
            graph.add_edge(k, j)
        elif nodes[j] == 'teal' and nodes[k] == 'red':
            graph.add_edge(k, j)
        else:
            graph.remove_edge(k, j)
    return graph

def solve_alternate(graph, source, target):
    graph = assign_weights_alternate(graph)
    return alternate(graph, source, target)
