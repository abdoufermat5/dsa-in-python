from base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using unordered list"""

    def __init__(self):
        """Create an empty map"""
        self._table: list["_Item"] = []

    def __getitem__(self, key):
        """ Return the value associated with the given key else raise KeyError"""
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError("Key Error:" + repr(key))

    def __setitem__(self, key, value):
        """
        Assign value to the given key or overwrite existing value if key already exists
        """
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        # Key does not exist
        return self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """
        Remove key from the table if exists otherwise raise KeyError
        """
        for j in range(len(self._table)):
            if self._table[j].key == key:
                self._table.pop(j)
                return

        # Not found
        raise KeyError("Key '%s' not found" % key)

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate an iterator over the table's keys"""
        for item in self._table:
            yield item._key


if __name__ == "__main__":
    test = UnsortedTableMap()
    test["a"] = 1
    test["b"] = 2
    test["c"] = 3
    test["d"] = 4

    print(*test, sep="\n")

    print(*test.items(), sep="\n")
