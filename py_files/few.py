import networkx as nx

def assign_weights_few(G):
    '''Given a networkx graph G, assigns weights to edges like so:
     - black to black node: 0
     - black to red node: 1
     - red to red node: 1
     returns the graph G with assigned weights'''

    # loop through edges
    for u, v in G.edges():
        node_colors = [G.nodes[u]['color'], G.nodes[v]['color']]
        if 'red' in node_colors:
            weight = 1
        else:
            weight = 0
        G.edges[u, v]['weight'] = weight
    
    return G

def count_reds(G, path):
    '''Given a graph and a list of nodes in a path within,
    iterates over the nodes and counts the number of red nodes
    returns the count'''
    
    count = 0
    for node in path:
        if G.nodes[node]['color'] == 'red':
            count += 1
    
    return count

def solve_few(G, s, t):
    '''Given networkx graph, solves few problem
    returns output specified by red-scare pdf'''

    G = assign_weights_few(G)

    try:
        path = nx.shortest_path(G, s, t, weight='weight')
    except:
        return -1
    else:
        return count_reds(G, path)
