from collections import defaultdict
import numpy as np


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


