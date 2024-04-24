from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1

        queue = deque([("0000", 0)])
        visited = set("0000")

        while queue:
            current, depth = queue.popleft()

            if current == target:
                return depth

            for i in range(4):
                for move in [-1, 1]:
                    new_digit = (int(current[i]) + move) % 10
                    new_combination = current[:i] + str(new_digit) + current[i + 1 :]

                    if (
                        new_combination not in visited
                        and new_combination not in dead_set
                    ):
                        visited.add(new_combination)
                        queue.append((new_combination, depth + 1))

        return -1


solution = Solution()
testcases = [
    [["0201", "0101", "0102", "1212", "2002"], "0202"],
    [["8888"], "0009"],
    [["8888"], "0000"],
    [["0000"], "8888"],
]

for deadends, target in testcases:
    print(solution.openLock(deadends, target))
