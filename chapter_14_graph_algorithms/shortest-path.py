from base import Graph, Vertex, AdaptableHeapPriorityQueue


def simple_shortest_path(g: Graph, src: Vertex):
    """
    Compute the shortest path distances from src to reachable vertices of g

    :param g: a graph that can be directed or undirected
    :param src: the source vertex
    :return: a dictionary mapping each reachable vertex to its distance from source
    """
    d = {}  # d[v] is the upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pq_locator = {}
    # intitialize
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float("inf")
        pq_locator[v]= pq.add(d[v], v)
    while not pq.is_empty():
        k, u = pq.remove_min()
        cloud[u] = k
        del pq_locator[u]
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                w = e.element()
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    pq.update(pq_locator[v], d[v], v)
    return cloud


def shortest_path_tree(g: Graph, s: Vertex, d: dict):
    """
    Reconstruct shortest-path tree rooted at vertex `s`, given distance map d.
    :param g: a graph
    :param s: source vertex
    :param d: dstance map
    :return: a tree
    """
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):  # only incoming
                u = e.opposite(v)
                w = e.element()
                if d[v] == d[u] + w:
                    tree[v] = e
    return tree


if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)

    g.insert_edge(v1, v3, 1)
    g.insert_edge(v2, v1, 5)
    g.insert_edge(v3, v2, 2)
    g.insert_edge(v1, v4, 4)
    g.insert_edge(v4, v5, 3)
    g.insert_edge(v5, v1, 1)

    d = simple_shortest_path(g, v1)
    tree = shortest_path_tree(g, v1, d)
    print(d)  # {1: 0, 3: 1, 5: 1, 2: 3, 4: 4}
    print(tree)  # {3: 1 -> 3, 5: 5 -> 1, 2: 3 -> 2, 4: 4 -> 5}
