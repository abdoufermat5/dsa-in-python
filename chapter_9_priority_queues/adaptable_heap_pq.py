from .heap_pq import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator based priority queue implemented with binary heap"""

    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the pq"""
        __slots__ = "_index"  # index as additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

        def __repr__(self):
            return f"({self._key}, {self._value}, {self._index})"

        # override swap method
    def __repr__(self):
        return str(self._data)

    def _swap(self, i, j):
        super()._swap(i, j)  # perform the swap
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        """
        The bubble utility determines whether to apply up-heap or down-heap bubbling,  depending on whether the given location
        has a parent with a smaller key
        :param j: position j
        :return: None
        """

        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))  # index of last leaf
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self, loc: "Locator", n_key, n_value):
        j = loc._index
        if not (0<=j<len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator!")

        loc._key, loc._value = n_key, n_value
        self._bubble(j)  # reinstate the heap order property

    def remove(self, loc):
        j = loc._index
        if not (0<=j<len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator!")
        if j == len(self) - 1:
            self._data.pop()  # just remove it

        else:
            self._swap(j, len(self) - 1)  # put item at last position
            self._data.pop()  # remove it
            self._bubble(j)  # reinstate the heap order property

        return loc._key, loc._value


if __name__ == "__main__":
    test = AdaptableHeapPriorityQueue()
    test.add(1, "A")
    test.add(2, "B")
    test.add(3, "C")
    test.add(-4, "D")
    test.add(0, "E")
    test.add(5, "F")
    test.add(-1, "G")

    print(test)
