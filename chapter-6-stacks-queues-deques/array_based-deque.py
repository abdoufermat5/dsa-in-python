from utils.empty import Empty


class ArrayDeque:
    """FIFO Queue implementation using a circular array as underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 5

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        f = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)

        self._size -= 1
        return f

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        back = (self._front + self._size - 1) % len(self._data)
        f = self._data[back]
        self._data[back] = None

        self._size -= 1
        return f

    def add_last(self, e):
        self._resize_default()
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        self._resize_default()
        back = (self._front - 1) % len(self._data)

        self._data[back] = e
        self._size += 1
        self._front = (self._front - 1) % len(self._data)

    def _resize_default(self):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

    def _resize(self, cap):
        old = self._data

        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


if __name__ == "__main__":
    q = ArrayDeque()
    for i in range(0, 9, 2):
        q.add_first(i)
        q.add_last(i**4)

    print(q.__dict__)
    q.add_last(5)
    print(q.__dict__)
    print("delete first", q.delete_first())
    print(q.__dict__)
    print("last: ", q.last())
    print("first: ", q.first())
    print("delete last", q.delete_last())
    print(q.__dict__)
