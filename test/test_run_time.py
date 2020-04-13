import src.run_time as rt
import unittest


class DSPUnitTest(unittest.TestCase):

    # Setting up for the test
    def setUp(self) -> None:
        self.root = 1
        self.array_dense = rt.array_dense(self.root)
        self.array_sparse = rt.array_sparse(self.root)
        self.heap_dense = rt.heap_dense(str(self.root))
        self.heap_sparse = rt.heap_sparse(str(self.root))

    def testDense(self):
        self.assertLess(self.array_dense, self.heap_dense)

    def testSparse(self):
        self.assertGreater(self.array_sparse, self.heap_sparse)


class HeapDelMin(unittest.TestCase):
    """
    (a) test case: to check the propriety of delete_min operation of MinHeap Class
    (b) test data: a random list of numbers [50, 26, 49, 21, 71, 21, 20, 48, 11, 56]
    (c) expected result: 11
    (d) actual result: program output
    """

    # Setting up for the test
    def setUp(self):
        self.random_list = [50, 26, 49, 21, 71, 21, 20, 48, 11, 56]
        self.delmin = MinHeap(self.random_list).delete_min()

    def testEqual(self):
        self.assertEqual(self.delmin, 11)



if __name__ == '__main__':
    unittest.main()