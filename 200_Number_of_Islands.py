from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []

        height = len(grid)
        width = len(grid[0])

        visited = set()

        for row in range(height):
            for col in range(width):
                island = set()
                self.dfs(grid, row, col, height, width, visited, islands, island)
                if island:
                    print(row, col)
                    print(island)
                    islands.append(island)

        return len(islands)

    def dfs(self, grid, row, col, height, width, visited, islands, island):
        if (row, col) in visited:
            return
        if not (-1 < row < height and -1 < col < width):
            return

        visited.add((row, col))

        if grid[row][col] != "1":
            return

        island.add((row, col))

        self.dfs(grid, row, col + 1, height, width, visited, islands, island)
        self.dfs(grid, row + 1, col, height, width, visited, islands, island)
        self.dfs(grid, row, col - 1, height, width, visited, islands, island)
        self.dfs(grid, row - 1, col, height, width, visited, islands, island)


test_cases = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ],
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
    [["1", "0", "1", "1", "0", "1", "1"]],
]

solution = Solution()

for grid in test_cases:
    print(solution.numIslands(grid))
