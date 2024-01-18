from base import TreeMap


class AVLTree(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = "_height"

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left._height is not None else 0

        def right_height(self):
            return self._right._height if self._right._height is not None else 0

    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _is_balanced(self, p):
        return abs(p._node.left_height() - p._node.right_height())<=1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        return self.right(p)

    def _tall_grandchild(self,p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)
