import time
from typing import Callable
import random


class LabelUnionFind:   # also called quick-find
    """Label each element with its set number."""
    def __init__(self, n: int):
        if n < 0: raise ValueError("Size must be non-negative.")
        self.label = list(range(n))

    def find(self, i: int) -> int:
        """Return the set containing i."""
        if i < 0 or i >= len(self.label):
            raise IndexError("Index out of bounds.")

        return self.label[i]

    def query(self, i: int, j: int) -> bool:
        """Return True if elements i and j are in the same set."""
        return self.find(i) == self.find(j)

    def union(self, i: int, j: int) -> None:
        """Merge the set containing j into the set containing i."""
        set_i = self.find(i)
        set_j = self.find(j)

        if set_i == set_j:
            return

        for k in range(len(self.label)):
            if self.label[k] == set_j:
                self.label[k] = set_i


class TreeUnionFind:    # also called quick-union
    """Organise each subset as a tree."""
    def __init__(self, n: int):
        if n < 0: raise ValueError("Size must be non-negative.")
        self.parent = [-1 for _ in range(n)] # use -1 to represent the root

    def find(self, i: int) -> int:
        """Find the root of the tree containing i."""
        if i < 0 or i >= len(self.parent):
            raise IndexError("Index out of bounds.")

        idx = i
        while self.parent[idx] != -1:
            idx = self.parent[idx]
        return idx

    def query(self, i: int, j: int) -> bool:
        """Return True if element i and j are under the same tree."""
        return self.find(i) == self.find(j)

    def union(self, i: int, j: int) -> None:
        """Attach the root of j's tree under the root of i's tree."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_j] = root_i


class UnionByWeight:    # also called weighted quick-union
    """Merge the smaller tree into the larger tree."""
    def __init__(self, n: int):
        if n < 0: raise ValueError("Size must be non-negative.")
        self.parent = [-1 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, i: int) -> int:
        """Find the root of the tree containing i."""
        if i < 0 or i >= len(self.parent):
            raise IndexError("Index out of bounds.")

        idx = i
        while self.parent[idx] != -1:
            idx = self.parent[idx]
        return idx

    def query(self, i: int, j: int) -> bool:
        """Return True if element i and j are under the same tree."""
        return self.find(i) == self.find(j)

    def union(self, i: int, j: int) -> None:
        """Attach the smaller tree to the larger tree."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return

        if self.size[root_i] <= self.size[root_j]:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]


class UnionByRank:      # also called weighted quick-union with path compression
    """Attach all nodes to the root directly for faster search."""
    def __init__(self, n: int):
        if n < 0: raise ValueError("Size must be non-negative.")
        self.parent = [-1 for _ in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i: int) -> int:
        """Return the root index and attach all nodes in
        the search path to the root."""
        if i < 0 or i >= len(self.parent):
            raise IndexError("Index out of bounds.")

        # Find the root
        root = i
        while self.parent[root] != -1:
            root = self.parent[root]

        # Point every point along the path to the root (path compression)
        curr = i
        while curr != root:
            nxt = self.parent[curr]
            self.parent[curr] = root
            curr = nxt

        return root

    def query(self, i: int, j: int) -> bool:
        """Return True if element i and j are under the same tree."""
        return self.find(i) == self.find(j)

    def union(self, i: int, j: int) -> None:
        """Attach the tree with lower rank to the other."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return

        if self.rank[root_i] == self.rank[root_j]:
            self.parent[root_i] = root_j
            self.rank[root_j] += 1
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i


# Default production implementation
UnionFind = UnionByRank


def benchmark_uf(
    uf_cls: Callable,
    n: int,
    worst_unions: list[tuple[int, int]],
    random_unions: list[tuple[int, int]],
    finds: list[int],
) -> tuple[float, float, float]:
    # 1. Worst Union (fresh instance)
    uf_worst = uf_cls(n)
    start = time.perf_counter()
    for i, j in worst_unions:
        uf_worst.union(i, j)
    worst_union_time = time.perf_counter() - start

    # 2. Find on the worst-case structure
    start = time.perf_counter()
    for i in finds:
        uf_worst.find(i)
    find_time = time.perf_counter() - start

    # 3. Random Union (fresh instance)
    uf_rand = uf_cls(n)
    start = time.perf_counter()
    for i, j in random_unions:
        uf_rand.union(i, j)
    random_union_time = time.perf_counter() - start

    return worst_union_time, random_union_time, find_time


if __name__ == "__main__":
    random.seed(42)
    n = 10_000
    worst_unions = [(i + 1, i) for i in range(n - 1)]
    random_unions = [(random.randrange(n), random.randrange(n)) for _ in range(n)]
    random_finds = [random.randrange(n) for _ in range(n)]

    print("Runtime comparison across four versions of union find:\n")
    print(f"| {'Method':<15} | {'Worst Union':<12} | {'Random Union':<12} | {'Worst Find':<12} |")
    print(f"|{'-' * 17}|{'-' * 14}|{'-' * 14}|{'-' * 14}|")
    for cls in (LabelUnionFind, TreeUnionFind, UnionByWeight, UnionByRank):
        worst_u, rand_u, find_t = benchmark_uf(cls, n, worst_unions, random_unions, random_finds)
        print(f"| {cls.__name__:<15} | {worst_u * 1000:>10.2f}ms | {rand_u * 1000:>10.2f}ms | {find_t * 1000:>10.2f}ms |")