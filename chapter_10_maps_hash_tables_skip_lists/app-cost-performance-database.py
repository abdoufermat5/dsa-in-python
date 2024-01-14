from sorted_table_map import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost performance) pairs"""

    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        """Returns (cost, performance) pair with largest cost not exceeding c"""

        return self._M.find_le(c)

    def add(self, c, p):
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)


if __name__ == "__main__":

    CPD = CostPerformanceDatabase()
    CPD.add(120000, 100)
    CPD.add(100000, 100)
    CPD.add(200000, 150)
    CPD.add(150000, 110)
    CPD.add(300000, 200)
    CPD.add(500000, 300)
    CPD.add(1000000, 500)
    CPD.add(250000, 100)

    print("Best I can afford with 190k$ : ", CPD.best(190000))

    print("Iterating over the database:")
    for item in CPD._M:
        print(item)