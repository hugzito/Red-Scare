from collections import deque
import networkx as nx
from few import count_reds

def assign_weights_many(G):
    '''Given a graph G, assigns weights to all edges
    if either node is red the weight becomes the negative of the total number of edges + 1
    if both nodes are black the weight becomes 0
    returns the graph G with the assigned weights'''

    n_edges = len(G.edges)+1
    # loop through edges
    for u, v in G.edges():
        node_colors = [G.nodes[u]['color'], G.nodes[v]['color']]
        if 'red' in node_colors:
            weight = -n_edges
        else:
            weight = 0
        G.edges[u, v]['weight'] = weight
    
    return G
def check_cycle(G):
    G.is_directed()
    nx.find_cycle(G)
    return '-'

def solve_many(G, s, t):
    '''Given networkx graph, solves many problem
    returns output specified by red-scare pdf'''
    try: return check_cycle(G)
    except:
        G = assign_weights_many(G)

        if nx.is_directed_acyclic_graph(G):
            try:
                path = nx.shortest_path(G, s, t, weight='weight', method='bellman-ford')
            except:
                return -1
            else:
                return count_reds(G, path)
        else:
            return '-'