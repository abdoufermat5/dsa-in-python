from utils.empty import Empty


class Node:
    __slots__ = "value", "next", "prev"

    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.prev = previous

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedBase:
    def __init__(self):
        self._header = Node()
        self._trailer = Node()
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _insert_between(self, e, prev, succ):
        n = Node(e, succ, prev)
        succ.prev = n
        prev.next = n
        self._size += 1

    def _delete_node(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self._size -= 1
        e = node.value
        node.prev = node.next = node.value = Node  # deprecating and gc
        return e


class LinkedDeque(DoublyLinkedBase):
    def first(self):
        if self.isEmpty():
            raise Empty("List is empty!")
        return self._header.next.value

    def last(self):
        if self.isEmpty():
            raise Empty("List is empty!")
        return self._trailer.prev.value

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer.prev, self._trailer)

    def delete_first(self):
        if self.isEmpty():
            raise Empty("List is empty!")
        self._delete_node(self._header.next)

    def delete_last(self):
        if self.isEmpty():
            raise Empty("List is empty!")
        self._delete_node(self._trailer.prev)


class PositionalList(DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def __repr__(self):
            return f"Position({self._node})"

        def element(self):
            return self._node.value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not self == other

    def __repr__(self):
        return f"PositionalList({[p for p in self]})"

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node.next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, prev, succ):
        node = super()._insert_between(e, prev, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original.prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old = node.value
        node.value = e
        return old

    def sort(self):
        if self.isEmpty():
            raise Empty("List is empty")
        marker = self.first()
        while marker != self.last():
            pivot = self.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != self.first() and self.before(walk).element() > value:
                    walk = self.before(walk)
                self.delete(pivot)
                self.add_before(walk, value)
