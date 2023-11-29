import networkx as nx

def get_colored_nodes(G, color="red"):
    '''
    Get a list of nodes with the color of reference
    '''

    colored_nodes = [x for x,y in G.nodes(data=True) if y['color']==color]
    return colored_nodes

def solve_none(G, s, t):
    '''
    remove all edges where a colored node is involved.
    then run a shortest path algorithm

    returns amount of nodes needed to get from s to t, including t
    '''


    G_none = G.copy()
    colored_nodes = get_colored_nodes(G)
    if s in colored_nodes:
        colored_nodes.remove(s)
    if t in colored_nodes:
        colored_nodes.remove(t)
    G_none.remove_edges_from(list(G.edges(colored_nodes)))
    try:
        shortest_path = nx.shortest_path(G_none, s, t)
    except:
        return -1
    return len(shortest_path) - 1