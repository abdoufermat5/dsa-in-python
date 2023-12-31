import copy
from base import Graph, Vertex


def floydWarshall(graph: Graph):
    closure = copy.deepcopy(graph)

    vertices = list(closure.vertices())
    n = len(vertices)

    for i in range(n):
        for k in range(n):
            if i != k and closure.get_edge(vertices[i], vertices[k]) is not None:
                for j in range(n):
                    if i != j != k and closure.get_edge(vertices[k], vertices[j]) is not None:
                        if closure.get_edge(vertices[i], vertices[j]) is None:
                            closure.insert_edge(vertices[i], vertices[j])

    return closure


if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)

    g.insert_edge(v1, v3, 1)
    g.insert_edge(v2, v1, 1)
    g.insert_edge(v3, v2, 1)
    g.insert_edge(v1, v4, 1)
    g.insert_edge(v4, v5, 1)

    cl = floydWarshall(g)
    print(list(cl.edges()))
