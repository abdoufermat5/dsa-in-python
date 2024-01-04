from queue import Queue

from base import Graph, Vertex


def simpleBFS(g: Graph, s: Vertex, discovered: dict):
    """Compute a simple BFS algorithm """
    level = [s]

    while len(level) > 0:
        n_lev = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = discovered[u] + e.element()
                    n_lev.append(v)

        level = n_lev


def queueBFS(g: Graph, s: Vertex, discovered: dict):
    """Compute a simple BFS algorithm using a FIFO queue"""

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()

        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = discovered[u] + e.element()
                q.put(v)


if __name__ == '__main__':
    g = Graph()
    v1 = g.insert_vertex(7)
    v2 = g.insert_vertex(13)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)

    g.insert_edge(v1, v3, 1)
    g.insert_edge(v2, v1, 1)
    g.insert_edge(v3, v2, 1)
    g.insert_edge(v1, v4, 1)
    g.insert_edge(v4, v5, 1)

    discovered = {v1: 0}
    queueBFS(g, v1, discovered)
    print(discovered)
