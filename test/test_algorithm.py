import unittest
import numpy as np
from src.ultilities import convert_to_graph
import networkx as nx
from src.dijkstra import Djikstrastpath
from src.tarjan import tarjanstpath
from src.ultilities import convert_to_adj_list
import random


class DSTpath(unittest.TestCase):
    """
    (a) test case: to check the result of the shortest distance of the shortest path using original Djikstra algorithm.
    (b) test data: graphs generated from main.py/ graph_generator.py
    (c) expected result: results from built-in networkx_dijkstra_path_length function
    (d) actual result: program output
    """

    txt_file = "../data/array/dense_weighted_matrix.txt"
    to_test_graph = np.loadtxt(txt_file, skiprows=2)
    nx_graph = nx.from_numpy_matrix(to_test_graph)

    to_test_graph[to_test_graph == 0] = np.inf

    source = 0
    target = 26

    def setUp(self):
        source = self.source
        target = self.target

        self.to_test_result = Djikstrastpath(self.to_test_graph, source, str(target))[0]
        self.nx_result = nx.dijkstra_path_length(self.nx_graph, source, target)

    def testDistance(self):
        self.assertEqual(float(self.to_test_result), float(self.nx_result))


class TSPth(unittest.TestCase):
    """
    (a) test case: to check the result of the shortest distance of the shortest path using Tarjan modification with heap.
    (b) test data: graphs generated from main.py/ graph_generator.py
    (c) expected result: results from built-in networkx_dijkstra_path_length function
    (d) actual result: program output
    """

    s_txt_file = "../data/heap/dense_stream_arcs.txt"
    a_txt_file = "../data/array/dense_weighted_matrix.txt"
    to_test_graph = convert_to_adj_list(s_txt_file)
    nx_graph = nx.from_numpy_matrix(np.loadtxt(a_txt_file, skiprows=2))

    source = 1
    target = 90

    def setUp(self):
        source = self.source
        target = self.target

        self.to_test_result = tarjanstpath(self.to_test_graph, str(source), str(target))[0]
        self.nx_result = nx.dijkstra_path_length(self.nx_graph, source, target)

    def testDistance(self):
        self.assertEqual(float(self.to_test_result), float(self.nx_result))


if __name__ == '__main__':
    unittest.main()
