# abstract base.py class for a tree
from queue import Queue


class Tree:
    """abstract base.py class representing a tree structure no order imposed"""

    # Position class
    class Position:
        def element(self):
            """return the element at the given position"""
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same position"""
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            """Return False if other Position does not represent the same position"""
            raise NotImplementedError("Must be implemented by subclass")

    # abstract methods
    def root(self):
        """Return Position representing the tree's root or None if empty"""
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        """Return the Position representing p's parent or None if p is root position"""
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that position p has"""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """Generate an interation of Positions representing p's children"""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("Must be implemented by subclass")

    # concrete methods
    def is_root(self, p):
        """Return True if p is the root Position of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if tree has no elements"""
        return len(self) == 0

    def depth(self, p):
        """the depth of a Position p is the number of ancestors of p so this
        function returns the number of ancestors of p
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def tree_height(self):
        """The height of a non-empty tree is the maximum between the depth of its leaf positions"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def subtree_height(self, p):
        """the height of a position p is one more than the maximum of the heights of p’s children so
        this function returns the height of a subtree rooted at position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.subtree_height(c) for c in self.children(p))

    def height(self, p=None):
        """Returns the height of the subtree rooted at position p"""
        if p is None:
            p = self.root()
        return self.subtree_height(p)

    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in the subtree rooted at position p"""

        yield p  # visit p before its subtrees
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.preorder()

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in the subtree rooted at position"""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p  # visit p after its subtrees

    def breadth_first(self):
        if not self.is_empty():
            q = Queue(maxsize=len(self))
            q.put(self.root())
            while not q.empty():
                p = q.get()
                yield p
                for c in self.children(p):
                    q.put(c)


class BinaryTree(Tree):
    """Abstract base.py class representing a binary tree structure"""

    # Additional abstract methods
    def left(self, p):
        """Returns a Position representing p's left child.

        Return None of no left child for p
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Returns a Position representing p's right child.

        Return None of no right child for p
        """
        raise NotImplementedError("must be implemented by subclass")

    # Concrete methods
    def sibling(self, p):
        """Returns a Position representing p's sibling or None if no sibling"""
        parent = self.parent(p)
        if parent is None:
            # root has no sibling
            return None

        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an interation of Positions representing p's children"""
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in the subtree rooted at p"""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
            yield p
            if self.right(p) is not None:
                for other in self._subtree_inorder(self.right(p)):
                    yield other

    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.inorder()
