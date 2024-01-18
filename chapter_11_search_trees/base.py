from chapter_8_trees import LinkedBinaryTree
from chapter_10_maps_hash_tables_skip_lists import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """
    Sorted Map implementation using binary search tree
    """

    # Override Position
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def _subtree_search(self, p, k):
        if p.key() == k:
            return p
        elif p.key() < k:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        else:
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        return p

    def _subtree_first_position(self, p):
        """Returns Position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(p)

        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_first_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_last_position(self.right(p))
        else:
            walk = p
            ancestor = self.parent(walk)
            while ancestor is not None and walk == self.right(ancestor):
                walk = ancestor
                ancestor = self.parent(walk)
            return ancestor

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key or None if empty"""

        if self.is_empty():
            return None
        else:
            p = self.first()
            return p.key(), p.value()

    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return p.key(), p.value()

    def find_range(self, start, stop):
        if self.is_empty():
            return None
        else:
            p = self.find_position(start)
            if p.key() < start:
                p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield p.key(), p.value()
                p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError("Key Error: " + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self.parent(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        p = self.first()
        if p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        self._validate(p)

        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement

        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError("Key Error: " + repr(k))

    def _rebalance_access(self, p):
        pass

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """Rotate position p above its parent"""

        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # single rotation of y
            self._rotate(y)
            return y
        else:  # double rotation of x
            self._rotate(x)
            self._rotate(x)
            return x
