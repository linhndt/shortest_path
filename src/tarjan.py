from src.heap import MinHeap
from src.ultilities import convert_to_adj_list
import numpy as np


def tarjanspathtree(graph, starting_node):
    """Create Shortest path tree using Tarjan method using a min heap."""

    solution_dict = {}

    for ending_node in graph.keys():
        pq, visited, distance = [(0, starting_node, [])], set(), {starting_node: 0}
        heap = MinHeap(pq)
        while pq:
            (cost, current_node, path) = heap.delete_min()
            if current_node not in visited:
                visited.add(current_node)
                path = path + [current_node]
                if current_node == ending_node:
                    solution_dict[ending_node] = (cost, path)

                for neighbor, weight in graph.get(current_node, ()):
                    if neighbor in visited:
                        continue
                    prev = distance.get(neighbor, None)
                    next = cost + weight
                    if prev is None or next < prev:
                        distance[neighbor] = next
                        heap.insert((next, neighbor, path))

    return solution_dict


def tarjanstpath(graph, starting_node, ending_node):
    """Create a shortest path from source to target using Tarjan method."""

    solution_dict = tarjanspathtree(graph, starting_node)

    spath = solution_dict[ending_node]

    return spath


def TarjanSPathTree():
    """Implementation of Shortest path tree using Tarjain method for a sparse graph."""

    file = "data/heap/sparse_stream_arcs.txt"
    graph = convert_to_adj_list(file)
    print("Our nodes in the graph is ", graph.keys())

    initial_node = input("Input node which you want to start with: ")

    while initial_node:

        if initial_node in graph.keys():

            spanning_tree = tarjanspathtree(graph, initial_node)

            print("----------Solution----------")
            for node, value in spanning_tree.items():
                print("Distance and path from node", initial_node, "to node", node, "is: ", value)

            choice = input("Do you want to choose another starting node? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    TarjanSPathTree()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to choose another starting node? (y/n): ")

            break

        else:
            print("Please input a proper starting node.")

        initial_node = input("Input node which you want to start with: ")
