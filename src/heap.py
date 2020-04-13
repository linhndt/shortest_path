from math import ceil
import heapq

class Heap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.heapify(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def heapify(self, arr):
        """
        Convert a given array into a min heap

        --- Parameters ---
            arr: input array of numbers
        """
        n = len(arr)
        for i in range(int(n / 2), -1, -1):
            self.sift_down(i, arr)

    def sift_up(self, i):
        # Get parent index of the current node
        parent = int(ceil(i / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = int(ceil(i / 2 - 1))

    def sift_down(self, i, arr):
        """
        Assuming sub trees are already min heaps, converts tree rooted at current indx into a min heap.
        :param indx: Index to check for min heap
        """
        # Get index of left and right child of indx node
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        smallest = i

        # check what is the smallest value node in indx, left child and right child
        if left_child < len(arr):
            if arr[left_child] < arr[smallest]:
                smallest = left_child
        if right_child < len(arr):
            if arr[right_child] < arr[smallest]:
                smallest = right_child

        # if indx node is not the smallest value, swap with the smallest child
        # and recursively call min_heapify on the respective child swapped with
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.sift_down(smallest, arr)

    def insert(self, value):
        """
        Inserts an element in the min heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.sift_up(self.heap_size)
        self.heap_size += 1

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap Underflow!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.sift_down(indx, self.heap)

        return self.heap.pop()

    def delete_min(self):
        """
        Extracts the minimum value from the heap
        :return: extracted min value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)

"""A Min heap is a complete binary tree [CBT] (implemented using array)
in which each node has a value smaller than its sub-trees"""

from math import ceil


class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        self.heap_size = 0
        if arr is not None:
            self.create_min_heap(arr)
            self.heap = arr
            self.heap_size = len(arr)

    def create_min_heap(self, arr):
        """
        Converts a given array into a min heap
        :param arr: input array of numbers
        """
        n = len(arr)

        # last n/2 elements will be leaf nodes (CBT property) hence already min heaps
        # loop from n/2 to 0 index and convert each index node into min heap
        for i in range(int(n / 2), -1, -1):
            self.sift_down(i, arr, n)

    def sift_down(self, indx, arr, size):
        """
        Assuming sub trees are already min heaps, converts tree rooted at current indx into a min heap.
        :param indx: Index to check for min heap
        """
        # Get index of left and right child of indx node
        left_child = indx * 2 + 1
        right_child = indx * 2 + 2

        smallest = indx

        # check what is the smallest value node in indx, left child and right child
        if left_child < size:
            if arr[left_child] < arr[smallest]:
                smallest = left_child
        if right_child < size:
            if arr[right_child] < arr[smallest]:
                smallest = right_child

        # if indx node is not the smallest value, swap with the smallest child
        # and recursively call min_heapify on the respective child swapped with
        if smallest != indx:
            arr[indx], arr[smallest] = arr[smallest], arr[indx]
            self.sift_down(smallest, arr, size)

    def insert(self, value):
        """
        Inserts an element in the min heap
        :param value: value to be inserted in the heap
        """
        self.heap.append(value)
        self.heap_size += 1

        indx = self.heap_size - 1

        # Get parent index of the current node
        parent = int(ceil(indx / 2 - 1))

        # Check if the parent value is smaller than the newly inserted value
        # if so, then replace the value with the parent value and check with the new parent
        while parent >= 0 and self.heap[indx] < self.heap[parent]:
            self.heap[indx], self.heap[parent] = self.heap[parent], self.heap[indx]
            indx = parent
            parent = int(ceil(indx / 2 - 1))

    def delete(self, indx):
        """
        Deletes the value on the specified index node
        :param indx: index whose node is to be removed
        :return: Value of the node deleted from the heap
        """
        if self.heap_size == 0:
            print("Heap is empty!!")
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.heap_size -= 1

        self.sift_down(indx, self.heap, self.heap_size)

        return self.heap.pop()

    def delete_min(self):
        """
        Extracts the minimum value from the heap
        :return: extracted min value
        """
        return self.delete(0)

    def print(self):
        print(*self.heap)



if __name__ == "__main__":
    a = {'1': {'2': 6, '3': 10, '4': 11}, '2': {'1': 6, '4': 3, '6': 6, '7': 12}, '3': {'1': 10, '4': 5, '5': 8, '9': 9},
     '4': {'1': 11, '2': 3, '3': 5, '5': 7, '6': 2, '9': 12}, '5': {'3': 8, '4': 7, '6': 4, '8': 2, '9': 3},
     '6': {'2': 6, '4': 2, '5': 4, '7': 7, '8': 9}, '7': {'2': 12, '6': 7, '8': 4, 'p': 11},
     '8': {'5': 2, '6': 9, '7': 4, 'p': 7}, '9': {'3': 9, '4': 12, '5': 3, 'p': 10}, 'p': {'8': 7, '9': 10, '7': 11}}

