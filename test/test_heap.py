import src.run_time as rt
import unittest
from src.heap import MinHeap
import heapq
import random
from src.ultilities import convert_to_graph
import networkx as nx


class Heap(unittest.TestCase):
    """
    (a) test case: to check the propriety of operations of MinHeap Class
    (b) test data: a random list of numbers
    (c) expected result: results from built-in class heapq
    (d) actual result: program output
    """
    random_list = random.sample(range(10, 100), 10)
    to_test_heap = MinHeap(random_list.copy())
    heapq.heapify(random_list)
    print(random_list)

    def testDelmin(self):
        self.assertEqual(self.to_test_heap.delete_min(), heapq.heappop(self.random_list))

    def testInsert(self):
        value = 10
        self.assertEqual(self.to_test_heap.insert(value), heapq.heappush(self.random_list, value))


if __name__ == '__main__':
    unittest.main()
