from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        class UnionFind:
            def __init__(self, n, edges):
                self.parents = [i for i in range(n)]
                self.ranks = [0] * n

                self.create(edges)

            def root(self, node):
                parent = self.parents[node]
                if parent == node:
                    return parent

                return self.root(parent)

            def union(self, start, end):
                root_start = self.root(start)
                root_end = self.root(end)

                if root_start == root_end:
                    return

                match self.compare_rank(root_start, root_end):
                    case 1:
                        self.parents[root_end] = self.parents[root_start]
                    case -1:
                        self.parents[root_start] = self.parents[root_end]
                    case 0:
                        self.parents[root_end] = self.parents[root_start]
                        self.ranks[root_start] += 1

            def create(self, edges):
                for start, end in edges:
                    self.union(start, end)

            def compare_rank(self, start, end):
                if self.ranks[start] > self.ranks[end]:
                    return 1
                elif self.ranks[start] < self.ranks[end]:
                    return -1
                else:
                    return 0

            def is_connected(self, source, destination):
                return self.root(source) == self.root(destination)

        union_find = UnionFind(n, edges)

        return union_find.is_connected(source, destination)


solution = Solution()
testcases = [
    [3, [[0, 1], [1, 2], [2, 0]], 0, 2],
    [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5],
    [
        10,
        [[2, 6], [4, 7], [1, 2], [3, 5], [7, 9], [6, 4], [9, 8], [0, 1], [3, 0]],
        3,
        5,
    ],
]

for tc in testcases:
    print(solution.validPath(*tc))
