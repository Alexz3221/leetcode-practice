class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        Rows = len(grid)
        Cols = len(grid[0])
        count = 0

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= Rows or
                col >= Cols or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count