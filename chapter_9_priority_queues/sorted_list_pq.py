from base import PriorityQueueBase
from utils.empty import Empty
from chapter_7_linked_lists.doubly_linked_list import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented using sorted list"""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        """Add a new key-value pair to the priority queue"""
        newest = self._Item(k, v)
        walk = self._data.last()

        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return tuple (k, v) of item with minimum key"""
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")

        item = self._data.delete(self._data.first())
        return item._key, item._value
