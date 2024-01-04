class PriorityQueueBase:
    """Abstract base class for Priority Queue"""

    class _Item:
        """
        Lightweight composite to store priority queue items
        """
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __repr__(self):
            return f"({self._key}, {self._value})"

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        """Return True if the queue is empty"""
        return len(self) == 0
