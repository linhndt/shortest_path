import sys


def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path btw start & end nodes in a graph"""
    # detect if first time through, set current distance to zero
    if not visited:
        distances[start]=0
    # if we've found our end node, find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor, sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k, sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)


graph = {'a': {'w': 14, 'x': 7, 'y': 9},
        'b': {'w': 9, 'z': 6},
        'w': {'a': 14, 'b': 9, 'y': 2},
        'x': {'a': 7, 'y': 10, 'z': 15},
        'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
        'z': {'b': 6, 'x': 15, 'y': 11}}


from src.ultilities import convert_to_adj_list

file = "/data/heap/ballyskate_layout.txt"
a = convert_to_adj_list(file)
print(a)
print(graph)
print(shortestpath(graph, 'x', 'z'))
from decimal import Decimal

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


