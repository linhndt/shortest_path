import src.run_time as rt
import unittest
from src.heap import MinHeap
import heapq


class Heap(unittest.TestCase):
    """
    (a) test case: to check the propriety of operations of MinHeap Class
    (b) test data: a random list of numbers [50, 26, 49, 21, 71, 21, 20, 48, 11, 56]
    (c) expected result: results from builtin class heapq
    (d) actual result: program output
    """
    random_list = [50, 26, 49, 21, 71, 21, 20, 48, 11, 56]
    to_test_heap = MinHeap(random_list.copy())
    heapq.heapify(random_list)

    def testDelmin(self):
        self.assertEqual(self.to_test_heap.delete_min(), heapq.heappop(self.random_list))

    def testInsert(self):
        value = 10
        self.assertEqual(self.to_test_heap.insert(value), heapq.heappush(self.random_list, value))


if __name__ == '__main__':
    unittest.main()
