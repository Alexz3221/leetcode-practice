class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        Rows = len(grid)
        Cols = len(grid[0])
        fMax = 0

        def dfs(row, col,) -> int:
            if row < 0 or col < 0 or row > Rows -1 or col > Cols -1 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area
        size = 0
        for i in range(Rows):
            for j in range(Cols):
                if(grid[i][j]) == 1:
                    size = dfs(i,j,)
                    if size > fMax:
                        fMax = size
        return fMax