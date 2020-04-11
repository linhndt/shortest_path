import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_dir_wei_graph(total_num_nodes, G):
    """Generate a directed graph with weight by using Barabasi_Albert method"""

    for i in range(1, total_num_nodes):
        # before adding nodes, first calculate probabilities of each node
        degrees = nx.degree(G)
        node_probabilities = {}
        for each in G.nodes():
            if G.order() == 1:
                node_probabilities[each] = 1
            else:

                # the probability of each nodes being attached is = degrees of each node/sum of degree
                node_probabilities[each] = degrees[each]/sum(dict(degrees).values())

        node_probabilities_cum = []

        # results of line below shows cum probability of each node, like [[0,0.2],[1,0.35],[2,0.50],[3,0.7],[4,1.0]]
        prev = 0
        for n, p in node_probabilities.items():
            temp = [n, prev+p]
            node_probabilities_cum.append(temp)
            prev = prev + p

        # if the random number r falls into the "windows",
        # then return that k value which indicates the target node we should attach to
        n = int(random.random()*10)
        target_list = []
        for j in range(n):
            prev_cum = 0
            r = random.random()
            k = 0
            while not(prev_cum < r <= node_probabilities_cum[k][1]):
                prev_cum = node_probabilities_cum[k][1]
                k += 1

            # after jump out of loop, we got value of k, that's what we need for the index of target node
            target_node = node_probabilities_cum[k][0]
            if not(target_node in target_list):
                target_list.append(target_node)

        # add node
        G.add_node(i)

        # add weight to the edges with random number
        for target in target_list:
            weight = random.randint(10, 30)
            G.add_weighted_edges_from([(target, i, weight)])

    return G


def graph_visualisation(graph):
    """Visualise the graph"""

    nx.draw(graph, with_labels=1)
    plt.show()


def convert_matrix_to_str(numpy_matrix):
    """Convert the matrix to a str"""

    string = ""

    for r in range(numpy_matrix.shape[0]):
        for l in range(numpy_matrix.shape[1]):
            value = numpy_matrix.item((r, l))
            if value != 0:
                string += str(r) + "," + str(l) + "," + str(value) + "\n"

    return string


def save_stream_arc_format(matrix, number_of_node):
    """Save the graph to a .txt file in form of stream of arcs"""

    mtx = convert_matrix_to_str(matrix)

    txt_file_name = "../data/heap/stream_arcs.txt"

    with open(txt_file_name, "w") as file:
        file.write("S\n")
        file.write(str(number_of_node) + "\n")
        file.write(mtx)

    print("Stream of arcs was saved in path: ", txt_file_name)


def save_matrix_format(matrix, number_of_node):
    """Save the graph to a .txt file in form of a weighted martrix"""

    txt_file_name = "../data/array/weighted_matrix.txt"

    with open(txt_file_name, "w") as file:
        file.write("S\n")
        file.write(str(number_of_node) + "\n")
        np.savetxt(file, matrix, fmt="%1d", delimiter="\t")

    print("Weighted martrix was saved in path: ", txt_file_name)


def graph_generator():

    # generate weighted graph:
    C = np.matrix([[0]])
    G = nx.from_numpy_matrix(C, create_using=nx.DiGraph)
    graph_size = int(input("Type the number of nodes you want in total:\n"))
    graph = generate_dir_wei_graph(graph_size, G)
    graph_visualisation(graph)

    # save graph to the form of a martix:
    graph_matrix = nx.to_numpy_matrix(graph)

    # save to txt files:
    save_stream_arc_format(graph_matrix, graph_size)
    save_matrix_format(graph_matrix, graph_size)


if __name__ == "__main__":

    """create a graph from a matrix start with 1 nodes No.0"""
    graph_generator()