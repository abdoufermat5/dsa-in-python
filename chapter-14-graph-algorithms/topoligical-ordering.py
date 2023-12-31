from queue import Queue

from base import Graph, Vertex


def topological_sort(g: Graph):
    """
    Sort a graph g in a topological order. If g has cycle the result will be incomplete.
    :param g: a DAG
    :return: a list of vertices of directed acyclic graph g in topological order
    """

    topo = []  # list of vertices in topological order
    ready = Queue()  # list of vertices that have no remaining constraints
    incount = {}  # track of in-degree for each vertex

    for v in g.vertices():
        incount[v] = g.degree(v, False)  # store number of incoming edges for each vertex v
        if incount[v] == 0:
            ready.put(v)
    print(incount)
    while not ready.empty():
        u = ready.get()  # u is free of constraints
        topo.append(u)

        for e in g.incident_edges(u, outgoing=True, sorted=True, reverse=True):
            v = e.opposite(u)
            incount[v] -= 1  # v has one less constraint without u
            if incount[v] == 0:
                ready.put(v)
    return topo


if __name__ == "__main__":
    g = Graph(directed=True)
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)

    g.insert_edge(v1, v3, 5)
    g.insert_edge(v1, v2, 3)
    g.insert_edge(v1, v4, 7)
    g.insert_edge(v4, v5, 1)

    cl = topological_sort(g)
    print(cl)
