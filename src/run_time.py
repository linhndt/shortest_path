import numpy as np
import time
from src.dijkstra import Dijkstraspathtree
from src.tarjan import tarjanspathtree
from src.ultilities import convert_to_adj_list

""" To calculate running time applying array/ heap data structure for each dense/ sparse graph."""


def array_dense(root):
    txt = "../data/array/dense_weighted_matrix.txt"
    adjacency_matrix = np.loadtxt(txt, skiprows=2)
    adjacency_matrix[adjacency_matrix == 0] = np.inf

    start_time = time.time()
    Dijkstraspathtree(adjacency_matrix, root)
    end_time = time.time()

    run_time = end_time - start_time

    return run_time


def array_sparse(root):
    txt = "../data/array/sparse_weighted_matrix.txt"
    adjacency_matrix = np.loadtxt(txt, skiprows=2)
    adjacency_matrix[adjacency_matrix == 0] = np.inf

    start_time = time.time()
    Dijkstraspathtree(adjacency_matrix, root)
    end_time = time.time()

    run_time = end_time - start_time

    return run_time


def heap_dense(root):
    txt = "../data/heap/dense_stream_arcs.txt"
    graph = convert_to_adj_list(txt)

    start_time = time.time()
    tarjanspathtree(graph, root)
    end_time = time.time()

    run_time = end_time - start_time

    return run_time


def heap_sparse(root):
    txt = "../data/heap/sparse_stream_arcs.txt"
    graph = convert_to_adj_list(txt)

    start_time = time.time()
    tarjanspathtree(graph, root)
    end_time = time.time()

    run_time = end_time - start_time

    return run_time


if __name__ == "__main__":

    root = 1
    print("Heap_sparse", heap_sparse(str(root)))
    print("Array_dense", array_dense(root))
    print("Array_sparse", array_sparse(root))
    print("Heap_dense", heap_dense(str(root)))
