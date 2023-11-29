from collections import deque
import networkx as nx
# class Many:
#     def __init__(self, G, s, t):
#         self.graph = G
#         self.source = s
#         self.target = t
#         self.result = 0

#     def solve(self):
#         if self.graph.is_directed() and not self.is_cyclic():
#             # Initialize all distances to INF (overestimating)
#             self.change_weights()

#             # Adjust start vertex if necessary for computing distances
#             self.result = self.relax() + 1 if self.get_start().is_red() else self.relax()

#     def change_weights(self):
#         nodes = deque()
#         root = self.get_start()
#         nodes.append(root)

#         # Set end-vertex to have distance as INF
#         self.get_end().set_distance(float('inf'))

#         visited = set()

#         while nodes:
#             node = nodes.popleft()
#             visited.add(node)
#             node.set_distance(float('inf'))

#             for edge in node.get_edges():
#                 if edge.get_end() not in visited:
#                     nodes.append(edge.get_end())

#         self.get_start().set_distance(0)

#     def is_cyclic(self):
#         if nx.is_directed(self.graph):
#             cycles = list(nx.simple_cycles(self.graph))
#             return len(cycles) > 0
#         else:
#             return False  # Assuming non-directed graphs are not cyclic
        



#     def relax(self):
#         nodes = deque()
#         root = self.graph.get_start()
#         nodes.append(root)
#         visited = set()

#         while nodes:
#             node = nodes.popleft()
#             visited.add(node)
#             node.set_discovered(True)

#             for edge in node.get_edges():
#                 end_node = edge.get_end()
#                 temp_value_is_red = -1 if end_node.is_red() else 0

#                 if node.get_distance() + temp_value_is_red < end_node.get_distance():
#                     end_node.set_distance(node.get_distance() + temp_value_is_red)

#             for edge in node.get_edges():
#                 to_node = edge.get_end()
#                 if to_node not in visited and to_node not in nodes:
#                     nodes.append(to_node)
#                     to_node.set_shortest_to(edge)

#         return abs(self.graph.get_end().get_distance())

#     def print_result(self):
#         if not self.graph.is_directed():
#             print("?!\t")
#         elif self.graph.get_end().get_distance() == float('inf'):
#             print("-1\t")
#         else:
#             print(self.result + "\t")

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