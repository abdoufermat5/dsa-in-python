from heap_pq import HeapPriorityQueue
from chapter_7_linked_lists.doubly_linked_list import PositionalList


def pq_sort(C, reverse=False, key=None):
    """Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        if key is None:
            P.add(element, element)
        else:
            P.add(key(element), element)
    for j in range(n):
        (k, v) = P.remove_min()
        if reverse:
            C.add_first(v)
        else:
            C.add_last(v)


if __name__ == "__main__":
    L = PositionalList()
    L.add_last(-5)
    L.add_last(2)
    L.add_last(3)
    L.add_last(1)
    L.add_last(4)
    pq_sort(L)
    print(L)
    pq_sort(L, reverse=True)
    print(L)
    L = PositionalList()
    L.add_last("A")
    L.add_last("e6")
    L.add_last("at")
    L.add_last("trA")
    L.add_last("c")
    L.add_last("45")
    L.add_last("B")
    pq_sort(L, key=str.lower)
    print(L)
    pq_sort(L, key=lambda x: ord(x[-1]))
    print(L)
