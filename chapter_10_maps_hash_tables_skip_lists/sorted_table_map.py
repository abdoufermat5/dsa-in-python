from base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """

        if high < low:
            return high + 1

        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j] != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return self._table[0]._key, self._table[0]._value
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return self._table[-1]._key, self._table[-1]._value
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return self._table[j]._key, self._table[j]._value
        return None

    def find_le(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            if self._table[j]._key == k:
                return self._table[j]._key, self._table[j]._value
            else:
                return self._table[j - 1]._key, self._table[j - 1]._value
        return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return self._table[j - 1]._key, self._table[j - 1]._value
        return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k.”"""
        j = self._find_index(k, 0, len(self._table) - 1)
        while j < len(self._table):
            if self._table[j]._key == k:
                j = j + 1
            else:
                return self._table[j]._key, self._table[j]._value
        return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop."""

        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield self._table[j]._key, self._table[j]._value
            j += 1
