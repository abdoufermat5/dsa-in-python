class EulerTour:
    """Abstract base class for performing Euler tour of a tree

    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    """

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(0), 0, [])

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position p
        :param p: Position of current node being visited
        :param d: depth of p in the tree
        :param path: list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()

        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class BinaryEulerTour(EulerTour):
    """ Abstract base class for performing Euler tour of a binary tree0

    This version includes an additional _hook_invisit method that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).
    """
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.is_left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)

        if self._tree.is_right(p) is not None:
            path.append(0)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()

        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


# ################ APPLICATIONS #################


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * " " + str(p.element()))


class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = ". ".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(", ", end="")
        print(p.element(), end="")
        if not self.tree().is_leaf():
            print(" (", end="")

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(")", end="")


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)
