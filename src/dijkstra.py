import numpy as np


def Dijkstraspathtree(matrix, start):
    length = len(matrix)
    permanent_vertices = [start]
    temporary_vertices = []

    solution_dict = {}
    dis = []

    dis.extend(matrix[start])
    temporary_vertices.extend(matrix[start])
    temporary_vertices[start] = np.inf

    path_parent = [start] * length
    while len(permanent_vertices) < length:
        i = temporary_vertices.index(min(temporary_vertices))
        temporary_vertices[i] = np.inf

        path = list()
        path.append(str(i))

        k = i
        while path_parent[k] != start:
            path.append(str(path_parent[k]))
            k = path_parent[k]
        path.append(str(start))
        path.reverse()

        permanent_vertices.append(i)
        for j in range(length):
            if j not in permanent_vertices:
                if (dis[i] + matrix[i][j]) < dis[j]:
                    dis[j] = temporary_vertices[j] = dis[i] + matrix[i][j]
                    path_parent[j] = i

        solution_dict[str(i)] = (dis[i], path)

    return solution_dict


def Djikstrastpath(matrix, start, end):

    solution_dict = Dijkstraspathtree(matrix, start)
    spath = solution_dict[end]

    return spath


def DjikstraSthTree():

    file = "data/array/dense_weighted_matrix.txt"
    adjacency_matrix = np.loadtxt(file, skiprows=2)
    adjacency_matrix[adjacency_matrix == 0] = np.inf

    print("Our nodes in the graph is from 0 to", len(adjacency_matrix) - 1)

    initial_node = int(input("Input node which you want to start with: "))

    while initial_node:

        if initial_node in range(len(adjacency_matrix)):

            spanning_tree = Dijkstraspathtree(adjacency_matrix, initial_node)

            print("----------Solution----------")
            for node, value in spanning_tree.items():
                print("Distance and path from node", initial_node, "to node", node, "is: ", value)

            choice = input("Do you want to choose another starting node? (y/n): ")

            while choice.lower() != 'n':

                if choice == "y":
                    DjikstraSthTree()

                else:
                    print("Please choose y or n")

                choice = input("Do you want to choose another starting node? (y/n): ")

            break

        else:
            print("Please input a proper starting node.")

        initial_node = input("Input node which you want to start with: ")

