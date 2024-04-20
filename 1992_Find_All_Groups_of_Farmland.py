from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        height = len(land)
        width = len(land[0])

        islands = []

        for row in range(height):
            for col in range(width):
                island = []
                self.dfs(land, row, col, height, width, island)
                if island:
                    islands.append(island)

        output = []

        for island in islands:
            min_land = min(island)
            max_land = max(island)
            output.append(
                [
                    min_land[0],
                    min_land[1],
                    max_land[0],
                    max_land[1],
                ]
            )
        return output

    def dfs(self, grid, row, col, height, width, island):
        if row == height or col == width or grid[row][col] == 0:
            return

        grid[row][col] = 0
        island.append((row, col))

        self.dfs(grid, row + 1, col, height, width, island)
        self.dfs(grid, row, col + 1, height, width, island)
        if row == height or col == width:
            return
        if grid[row][col] == 0:
            return

        grid[row][col] = 0
        island.append((row, col))

        self.dfs(grid, row + 1, col, height, width, island)
        self.dfs(grid, row, col + 1, height, width, island)


solution = Solution()

testcases = [
    [[1, 0, 0], [0, 1, 1], [0, 1, 1]],
    [[1, 1], [1, 1]],
    [[0]],
    [[1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0]],
]

for tc in testcases:
    print(solution.findFarmland(tc))
