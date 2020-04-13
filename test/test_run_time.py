"""
(a) test case: to check running time of shortest path program blabla
(b) test data: graph built from Preferential Attachment
(c) expected result: blabla
(d) actual result: program output

To run: python -m unittest DSPUnitTest
"""
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


if __name__ == '__main__':
    unittest.main()