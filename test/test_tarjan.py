from src.heap import Heap, MinHeap
from src.ultilities import convert_to_adj_list
import numpy as np


def tarjanspathtree(graph, starting_node):

    solution_dict = {}

    for ending_node in graph.keys():
        pq, visited, distance = [(0, starting_node, [])], set(), {starting_node: 0}
        while pq:
            heap = MinHeap(pq)
            (cost, current_node, path) = heap.extract_min()
            if current_node not in visited:
                visited.add(current_node)
                path = [current_node] + path
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

    pq, visited, distance = [(0, starting_node, [])], set(), {starting_node: 0}
    while pq:
        heap = MinHeap(pq)
        (cost, current_node, path) = heap.extract_min()
        if current_node not in visited:
            visited.add(current_node)
            path = [current_node] + path
            if current_node == ending_node:
                return cost, path

            for neighbor, weight in graph.get(current_node, ()):
                if neighbor in visited:
                    continue
                prev = distance.get(neighbor, None)
                next = cost + weight
                if prev is None or next < prev:
                    distance[neighbor] = next
                    heap.insert((next, neighbor, path))

    return np.inf, []


def TarjanSPathTree():

    file = "../data/heap/ballyskate_layout.txt"
    graph = convert_to_adj_list(file)
    print("Our nodes in the graph is:", *graph.keys())

    # initial_node = input("Input node which you want to start with: ")

    # if initial_node in graph.keys():
    #
    #     spanning_tree = tarjanspathtree(graph, initial_node)
    #
    #     print("----------Solution----------")
    #     for node, value in spanning_tree.items():
    #         print("Node ", node, ":")
    #         print("Distance and path from ", "node ", initial_node, " is: ", value)
    #
    # else:
    #     print("Please input a proper starting node.")
    #     TarjanSPathTree()


    while True:
        initial_node = input("Input node which you want to start with: ")

        if initial_node in graph.keys():

            spanning_tree = tarjanspathtree(graph, initial_node)

            print("----------Solution----------")
            for node, value in spanning_tree.items():
                print("Node ", node, ":")
                print("Distance and path from ", "node ", initial_node, " is: ", value)

            choice = input("Do you want to continue? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    TarjanSPathTree()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to continue? (y/n): ")

            break

        else:
            print("Please input a proper starting node.")
            TarjanSPathTree()


if __name__ == "__main__":

    file = "../data/heap/ballyskate_layout.txt"
    graph = convert_to_adj_list(file)
    print(graph)
    print(tarjanspathtree(graph, '1'))
    print(tarjanstpath(graph, '1', 'p'))

    TarjanSPathTree()