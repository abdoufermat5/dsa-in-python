from collections.abc import Iterable


class Vertex:
    __slots__ = "_element"

    def __init__(self, x):
        self._element = x

    def __str__(self):
        return str(self._element)

    def __repr__(self):
        return str(self._element)

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


class Edge:
    __slots__ = "_origin", "_destination", "_element"

    def __init__(self, u, v, x=None):
        self._origin = u
        self._destination = v
        self._element = x

    def __str__(self):
        return str(self._origin) + " -> " + str(self._destination)

    def __repr__(self):
        return str(self._origin) + " -> " + str(self._destination)

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        return self._destination if v is self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Returns True if the graph is directed"""
        return self._outgoing is not self._incoming

    def vertex_count(self):
        """Returns the number of vertices in the graph"""
        return len(self._outgoing)

    def vertices(self) -> Iterable[Vertex]:
        """Return an iteration of all vertices in the graph"""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self) -> Iterable[Edge]:
        """Return a set of all edges of the graph"""
        result = set()

        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v) -> Edge:
        """Return the edge from u to v or None if there is no adjacent"""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Returns the number of (outgoing) edges incident to vertex v in the graph
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True, **kwargs) -> Iterable[Edge]:

        """Return all (outgoing) edges incident to vertex v in the graph
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        adj_values = list(adj[v].values())
        if "sorted" in kwargs:
            if "reverse" in kwargs:
                adj_values.sort(key=lambda e: e.element(), reverse=kwargs["reverse"])
            else:
                adj_values.sort(key=lambda e: e.element())
        for edge in adj_values:
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x"""
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x"""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def transpose(self) -> "Graph":
        if self.is_directed():
            g = Graph(directed=True)
            g._outgoing = self._incoming
            g._incoming = self._outgoing
            return g
        else:
            return self


class Partition:
    """
    Union-find structure for maintaining disjoint sets.
    """

    class Position:
        __slots__ = "_container", "_element", "_size", "_parent"

        def __init__(self, container, e):
            self._container = container
            self._element = e
            self._size = 1
            self._parent = self  # convention for a group leader

        def element(self):
            return self._element

    def make_group(self, e):
        return self.Position(self, e)

    def find(self, p: Position):
        if p._parent != p:
            p._parent = self.find(p._parent)

        return p._parent

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)

        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += a._size

            else:
                a._parent = b
                b._size += a._size
