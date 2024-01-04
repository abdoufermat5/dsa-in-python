from utils.empty import Empty
from .base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)

        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self, contents=[]):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self._data) - 1)  # start at Parent of last leaf
        for j in range(start, -1, -1):
            self._downheap(j)

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        self._data.append(self._Item(k, v))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        item = self._data[0]

        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)

        return item._key, item._value


if __name__ == "__main__":
    test = HeapPriorityQueue([(2, "B"), (-3, "C"), (4, "D"), (2, "E"), (6, "F"), (1, "A")])
    print("min key-value pair: ", test.min())
    print("adding (-100, 'G')")
    test.add(-100, "G")
    print("min key-value pair: ", test.min())
    print(test._data)
    print("removing min key-value pair", test.remove_min())
    print(test._data)
