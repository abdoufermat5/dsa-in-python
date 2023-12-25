import random

from empty import Empty


class ArrayQueue:
    """FIFO Queue implementation using a circular array as underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = random.randint(0, ArrayQueue.DEFAULT_CAPACITY - 1)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        f = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)

        self._size -= 1
        return f

    def enqueue(self, e):
        # here len return the len of the list not the size of the queue!! so it's not the same as our __len__ above
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        while cap < self._size:
            self.dequeue()
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0




if __name__ == "__main__":
    q = ArrayQueue()
    for i in range(9):
        q.enqueue(i)

    print(q.__dict__)
    q.enqueue(9)
    print(q.__dict__)
    q.enqueue(10)
    print(q.__dict__)
