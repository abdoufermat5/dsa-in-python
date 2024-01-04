from utils.empty import Empty


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Empty("List is empty")
        return self.head

    def last(self):
        if self.is_empty():
            raise Empty("List is empty")
        return self.tail

    def add_first(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = None
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def add_last(self, value):
        node = Node(value)
        node.next = None
        if self.tail is None:
            self.tail = node
            self.head = node
            self.tail.next = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty("The list is empty!")
        n = self.head
        self.head = self.head.next
        self.size -= 1

        return n


if __name__ == "__main__":
    s = SinglyLinkedList()
    s.add_first(1)
    s.add_first(2)
    s.add_first(3)
    s.add_last(4)
    s.add_last(-1)
    s.add_last(50)

    print(s.head.value)
    print(s.tail.value)
    print(s.remove_first().value)
    print(s.last())
