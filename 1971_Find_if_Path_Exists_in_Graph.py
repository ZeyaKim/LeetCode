from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {num: [] for num in range(n)}
        visited = set()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def visit(cur, reached):
            if reached or cur in visited:
                return 0
            if cur == destination:
                reached = True
                return 1
            visited.add(cur)

            return sum(visit(dest, reached) for dest in graph[cur])

        return 0 < visit(source, False)


solution = Solution()
testcases = [
    [3, [[0, 1], [1, 2], [2, 0]], 0, 2],
    [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5],
]

for tc in testcases:
    print(solution.validPath(*tc))
