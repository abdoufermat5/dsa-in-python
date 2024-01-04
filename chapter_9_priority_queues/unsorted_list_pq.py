from base import PriorityQueueBase
from utils.empty import Empty
from chapter_7_linked_lists.doubly_linked_list import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise Empty("Priority Queue is empty")

        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return tuple (k, v) of item with minimum key"""
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        """Remove and return tuple (k, v) of item with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value
