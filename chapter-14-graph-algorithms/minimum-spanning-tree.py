from base import Graph, Vertex, Edge, AdaptableHeapPriorityQueue, Partition


def mst_prim_jarnik(g: Graph):
    """
    Compute a minimum spanning tree of weighted graph g.

    :param g: Graph
    :return: mst of graph g
    """

    d = {}  # is bound on distance to tree
    tree = []  # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()
    pq_locator = {}
    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float("inf")
        pq_locator[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        k, value = pq.remove_min()

        u, edge = value
        del pq_locator[u]
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pq_locator:
                w = link.element()
                if w < d[v]:
                    d[v] = w
                    pq.update(pq_locator[v], d[v], (v, link))

    # print(d)
    return tree


def mst_kruskal(g: Graph):
    """
    Compute a MST of a graph g using Kruskal'a algorithm
    :param g:
    :return:
    """
    tree = []
    pq = AdaptableHeapPriorityQueue()
    forest = Partition()
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)

    size = g.vertex_count()

    while len(tree) != size - 1 and not pq.is_empty():
        w, e = pq.remove_min()
        u, v = e.endpoints()

        a = forest.find(position[u])
        b = forest.find(position[v])

        if a != b:
            tree.append(e)
            forest.union(a, b)
    return tree


if __name__ == "__main__":
    g = Graph()
    v0 = g.insert_vertex(0)
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)
    v6 = g.insert_vertex(6)
    v7 = g.insert_vertex(7)
    v8 = g.insert_vertex(8)

    g.insert_edge(v0, v1, 4)
    g.insert_edge(v0, v7, 8)
    g.insert_edge(v1, v2, 8)
    g.insert_edge(v1, v7, 11)
    g.insert_edge(v2, v3, 7)
    g.insert_edge(v2, v8, 2)
    g.insert_edge(v2, v5, 4)
    g.insert_edge(v3, v4, 9)
    g.insert_edge(v3, v5, 14)
    g.insert_edge(v4, v5, 10)
    g.insert_edge(v5, v6, 2)
    g.insert_edge(v6, v7, 1)
    g.insert_edge(v6, v8, 6)
    g.insert_edge(v7, v8, 7)

    tree = mst_prim_jarnik(g)
    tree_k = mst_kruskal(g)

    print(tree)
    print(tree_k)
