from empty import Empty


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty array"""
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data[-1]


