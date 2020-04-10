from collections import defaultdict
import numpy as np


def convert_to_adj_list(file):
    """Convert stream of arcs in a txt file to an adjacency list """
    arc_stream = np.loadtxt(file, skiprows=2, delimiter=",", dtype={'names': ('nodeu', 'nodev', 'weight'),
                                                           'formats': ('S2', 'S2', 'i4')})

    graph_dict = defaultdict(list)

    for u, v, weight in arc_stream:
        u = u.decode('utf-8')
        v = v.decode('utf-8')
        graph_dict[u].append((v, weight))

    # for arc in arc_stream:
    #     node_u = arc[0].decode('utf-8')
    #     node_v = arc[1].decode('utf-8')
    #     weight = arc[2]
    #     graph_dict.setdefault(node_u, []).append([node_v, weight])

    # for key, value in graph_dict.items():
    #     keys = []
    #     values = []
    #     for i in value:
    #         keys.append(i[0])
    #         values.append(i[1])
    #         data = dict(zip(keys, values))
    #         graph_dict[key] = root_choice = input()data

    return graph_dict


