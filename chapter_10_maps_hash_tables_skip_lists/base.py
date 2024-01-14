import random
from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """
    Custom abc that includes a nonpublic _Item class
    """

    # -------------------------- Nested _Item class --------------------------------
    class _Item:
        """
        Lightweight composite to store a k-v pairs as map items
        """
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self._key == other._key)

        def __le__(self, other):
            return self._key < other._key


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash table map"""
        self._table = [None] * cap
        self._n = 0
        self._prime = p  # prime for MAD compression
        self._scale = 1 + random.randrange(p - 1)  # scale for MAD compression (the a!=0 constant)
        self._shift = random.randrange(p - 1)  # shift for MAD compression (the b constant)

    def _hash_function(self, k):
        return ((hash(k) * self._scale + self._shift) % self._prime) % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table)//2:  # keep load factor <= 0.5
            self._resize(2*len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for k, v in old:
            self[k] = v

