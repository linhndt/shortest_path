from collections import defaultdict
import numpy as np
import networkx as nx


def convert_to_adj_list(file):
    """Convert stream of arcs in a txt file to an adjacency list """
    arc_stream = np.loadtxt(file, skiprows=2, delimiter=",", dtype={'names': ('nodeu', 'nodev', 'weight'),
                                                           'formats': ('S25', 'S25', 'i4')})

    graph_dict = defaultdict(list)

    for u, v, weight in arc_stream:
        u = u.decode('utf-8')
        v = v.decode('utf-8')
        graph_dict[u].append((v, weight))

    return graph_dict


def convert_to_graph(file):
    """Convert stream of arcs in a txt file to an graph """
    arc_stream = np.loadtxt(file, skiprows=2, delimiter=",", dtype={'names': ('nodeu', 'nodev', 'weight'),
                                                           'formats': ('S25', 'S25', 'i4')})

    graph_dict = defaultdict(list)

    for u, v, weight in arc_stream:
        u = u.decode('utf-8')
        v = v.decode('utf-8')

        if u not in graph_dict.keys():
            graph_dict[u] = {}
        if v not in graph_dict.keys():
            graph_dict[v] = {}

        graph_dict[u][v] = weight
        graph_dict[v][u] = weight

    graph = nx.Graph(graph_dict)
    return graph


coverted_graph = convert_to_graph("../data/heap/dense_stream_arcs.txt")
