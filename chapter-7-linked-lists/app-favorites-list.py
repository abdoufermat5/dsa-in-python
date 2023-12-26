from .doubly_linked_list import PositionalList


class FavoritesList:
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element().value != e:
            walk = self._data.after(walk)

        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))  # delete and reinsert

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(e) # place new at end
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate a sequence of top k elements in terms of access count"""
        if not 1<=k<=len(self):
            raise ValueError("Illegal value for k!")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)