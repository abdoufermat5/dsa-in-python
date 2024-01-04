from base import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing a position of a single node"""

        def __init__(self, container, node):
            """should not be called directly"""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for the given node or None if no node"""
        return self.Position(self, node) if node is not None else None

    # Binary tree constructor
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # public accessors
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size

    def root(self):
        """Return the position of the root node"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of the parent node of p or None if p is root"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child or None if no left"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child or None if no right"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of node at Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # setters

    def _add_root(self, e):
        """Place element e at the root of the empty tree and return new Position"""
        if self._root is not None: raise ValueError("Root already exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child Position for node at Position p with element e.

        Return Position of e or raise ValueError if p has already a left child"""

        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists")
        else:
            node._left = self._Node(e, node)
            self._size += 1
            return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child Position for node at Position p with element e.

        Return Position of e or raise ValueError if p has already a right child"""

        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child already exists")
        else:
            node._right = self._Node(e, node)
            self._size += 1
            return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace element at Position p with e and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete node at Position p and replace it with its child if any

        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or has two children"""

        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Invalid! p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:  # is this really necessary here??
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # weird to me
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external node at Position p (a leaf node)"""
        node = self._validate(p)

        if not self.is_leaf(p): raise ValueError("p must be a leaf")
        if not type(self) is type(t1) is type(t2): raise TypeError("Trees types must be the same")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


if __name__ == "__main__":
    # test the LinkedBinaryTree class
    # create a mock tree with 7 nodes
    t = LinkedBinaryTree()
    root = t._add_root(0)
    t._add_left(root, 1)
    t._add_right(root, 2)
    left = t.left(root)
    t._add_left(left, 3)
    t._add_right(left, 4)
    right = t.right(root)
    t._add_left(right, 5)
    t._add_right(right, 6)

    # informations about the tree
    print("Tree height: ", t.height())
    print("Tree size: ", len(t))
    print("Root: ", t.root().element())
    print("num_children(root): ", t.num_children(root))
    # test the public accessors
    assert len(t) == 7
    assert t.root().element() == 0
    assert t.left(t.root()).element() == 1
    assert t.right(t.root()).element() == 2
    print("All tests passed")
