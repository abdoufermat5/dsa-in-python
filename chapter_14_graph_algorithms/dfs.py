from base import Vertex, Edge, Graph


def simpleDFS(g: Graph, u: Vertex, discovered):
    """
    Perform simpleDFS of the undiscovered portion of the graph g starting at vertex u.

    :param g: Graph
    :param u: Vertex
    :param discovered: dictionary mapping each vertex to the edge that was used to discover it.
    :return: None
    """
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if discovered[v] is None:
            discovered[v] = e
            simpleDFS(g, v, discovered)


def simpleDFS_2(g, u, v, discovered):
    """Same as above but this time we check if there's a path between two vertices in the graph."""
    if u == v:  # base case: we have reached the destination vertex
        return True
    for e in g.incident_edges(u):
        x = e.opposite(u)
        if not discovered.get(x, False):
            discovered[x] = True
            if simpleDFS_2(g, x, v, discovered):
                # second base case destination vertex is the last visited vertex
                return True
    return False


def path(g, u, v):
    """Return true if there is a path between u and v in graph g else False"""
    discovered = {u: True}
    return simpleDFS_2(g, u, v, discovered)


def reconstruct_path(u, v, discovered):
    """To find if there's a direct path from u to v we can go through discovered.
    discovered looks like this: {1: None, 2: 1 -> 2, 4: 2 -> 4, 15: 4 -> 15, 8: 8 -> 15, 6: 15 -> 6, 7: 6 -> 7}

    for example if u=1 v=7
    we can walk from 7 to 1 which is the path from 1 to 7
    """
    path = []
    try:
        if v in discovered:
            path.append(v)
            walk = v
            while walk != u:
                e = discovered[walk]
                parent = e.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse()
            return path
    except:
        return False


def simpleDFS_complete(g: Graph):
    """Perform simpleDFS for entire graph and return forest a dictionary.

    Result maps each vertex to the edge that was used to discover it.
    (Vertices that are roots of a simpleDFS tree are mapped to None)."""
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            simpleDFS(g, u, forest)
    return forest


def findSCC(g: Graph):
    """This algorithms runs in O(n**3) where n is the number of vertices"""
    result = []

    is_scc = {u: False for u in g.vertices()}

    for u in g.vertices():

        if not is_scc[u]:

            scc = [u]
            for v in g.vertices():

                if v is not u and path(g, u, v) and path(g, v, u):
                    scc.append(v)
                    is_scc[v] = True
            result.append(scc)
    return result


def kosarajuSCC(g: Graph, u):
    """Check whether a graph is strongly connected or not. This runs in O(n+m) where n
    is the number of vertices in the graph and m is the number of edges"""

    discov1 = {x: None for x in g.vertices()}
    simpleDFS(g, u, discov1)
    print(discov1)
    n = sum(1 for x in discov1 if discov1[x] is None)
    if n != 0:
        return False

    gT = g.transpose()

    discov2 = {x: None for x in g.vertices()}
    simpleDFS(gT, u, discov2)
    print(discov2)
    n = sum(1 for x in discov2 if discov2[x] is None)
    if n != 0:
        return False

    return True


if __name__ == '__main__':
    # create a simple test graph and perform a simpleDFS traversal
    g = Graph(directed=True)
    v1 = g.insert_vertex(1)
    v2 = g.insert_vertex(2)
    v3 = g.insert_vertex(3)
    v4 = g.insert_vertex(4)
    v5 = g.insert_vertex(5)

    g.insert_edge(v1, v3)
    g.insert_edge(v2, v1)
    g.insert_edge(v3, v2)
    g.insert_edge(v1, v4)
    g.insert_edge(v4, v5)

    # discovered = {u: None}
    # simpleDFS(g, v1, discovered)
    # print(discovered)
    print(path(g, v3, v1))
    # forest = simpleDFS_complete(g)
    # print("Forest from g: ", forest)
    # print("Number of connected components: ", sum(1 for u in forest if forest[u] is None))

    print("strongly connected components: ", findSCC(g))
    print("Is g strongly connected", kosarajuSCC(g, v1))
