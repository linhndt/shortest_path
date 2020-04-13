import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_dir_wei_sparse_graph(total_num_nodes, G):
    """The funcion generate a sparse directed graph with weight by using Barabasi_Albert method"""
    for i in range(1, total_num_nodes):
        # before adding nodes, first calculate probabilities of each node
        degrees = nx.degree(G)
        node_probabilities = {}
        for each in G.nodes():
            if G.size() == 0:
                node_probabilities[each] = 1
            else:
                # the probability of each nodes being attached is = degrees of each node/sum of degree
                node_probabilities[each] = degrees[each] / sum(dict(degrees).values())
        node_probabilities_cum = []
        # results of line below shows cumulated probability of each node, like [[0,0.2],[1,0.35],[2,0.50],[3,0.7],[4,1.0]]
        prev = 0
        for n, p in node_probabilities.items():
            temp = [n, prev + p]
            node_probabilities_cum.append(temp)
            prev = prev + p

        # if the random number r falls into the "windows", then return that k value which indicates the target node we should attach to

        n = 1
        target_list = []

        for j in range(n):
            prev_cum = 0
            r = random.random()
            k = 0
            while (not (r > prev_cum and r <= node_probabilities_cum[k][1])):
                prev_cum = node_probabilities_cum[k][1]
                k += 1
            # after jump out of loop, we got value of k, that's what we need for the index of target node
            target_node = node_probabilities_cum[k][0]
            if not (target_node in target_list):
                target_list.append(target_node)

        # adding node
        G.add_node(i)
        # adding weight to the edges with random number
        for target in target_list:
            weight = random.randint(10, 30)
            G.add_weighted_edges_from([(target, i, weight)])
    return G


def generate_dir_wei_dense_graph(total_num_nodes, G):
    """The funcion generate a directed graph with weight by using Barabasi_Albert method"""

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
        n = G.order()
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


def generate_graph_martrix(n, m):

    graph = nx.barabasi_albert_graph(n, m)
    graph_mtrx = nx.to_numpy_matrix(graph)

    return graph_mtrx


def convert_matrix_to_str(numpy_matrix):
    """Convert the matrix to a str"""

    string = ""

    for r in range(numpy_matrix.shape[0]):
        for l in range(numpy_matrix.shape[1]):
            value = numpy_matrix.item((r, l))
            if value != 0:
                string += str(r) + "," + str(l) + "," + str(value) + "\n"

    return string


def save_stream_arc_format(matrix, number_of_node, txt_file_name):
    """Save the graph to a .txt file in form of stream of arcs"""

    mtx = convert_matrix_to_str(matrix)

    with open(txt_file_name, "w") as file:
        file.write("S\n")
        file.write(str(number_of_node) + "\n")
        file.write(mtx)

    print("Stream of arcs was saved in path: ", txt_file_name)


def save_matrix_format(matrix, number_of_node, txt_file_name):
    """Save the graph to a .txt file in form of a weighted martrix"""

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

    # sparse graph
    sparse_graph = generate_dir_wei_sparse_graph(graph_size, G)
    # save graph to the form of a matrix:
    sparse_graph_matrix = nx.to_numpy_matrix(sparse_graph)

    # save to txt files:
    txt_file_name_array_sparse = "data/array/sparse_weighted_matrix.txt"
    txt_file_name_stream_sparse = "data/heap/sparse_stream_arcs.txt"
    save_stream_arc_format(sparse_graph_matrix, graph_size, txt_file_name_stream_sparse)
    save_matrix_format(sparse_graph_matrix, graph_size, txt_file_name_array_sparse)

    # dense graph
    dense_graph = generate_dir_wei_dense_graph(graph_size, G)
    # save graph to the form of a matrix:
    dense_graph_matrix = nx.to_numpy_matrix(dense_graph)

    # save to txt files:
    txt_file_name_array_dense = "data/array/dense_weighted_matrix.txt"
    txt_file_name_stream_dense = "data/heap/dense_stream_arcs.txt"
    save_stream_arc_format(dense_graph_matrix, graph_size, txt_file_name_stream_dense)
    save_matrix_format(dense_graph_matrix, graph_size, txt_file_name_array_dense)


if __name__ == "__main__":
    graph_generator()

