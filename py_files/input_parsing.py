import networkx as nx
from itertools import islice

def create_network(filepath):
    '''Given the filepath of an input file,
    Reads inputs into a networkx directed/undirected graph
    Nodes will have the attribute "color", with either "red" or "teal" as the values
    returns the graph, s and t nodes'''

    G = nx.Graph()

    # reading inputs into workable variables
    with open(filepath) as input_file:

        # first 2 lines
        head = list(islice(input_file, 2))
        
        n, e, r = head[0].replace('\n', '').split(' ')
        s, t = head[1].replace('\n', '').split(' ')

        # node lines
        nodes = list(islice(input_file, int(n)))
        for node in nodes:
            node = node.replace('\n', '').strip().split(' ')

            if len(node) == 2: # node is red
                G.add_node(node[0], color='red')
            else:
                G.add_node(node[0], color='teal')
        
        # edge lines
        edges = list(islice(input_file, int(e)))
        if edges: # some inputs have no edges so simply dont add anything
            if '->' in edges[0]:
                G = G.to_directed()

            for edge in edges:
                edge = edge.replace('\n', '').split(' ')
                G.add_edge(edge[0], edge[2])

        return G, s, t
