class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        Rows = len(grid)
        Cols = len(grid[0])
        islands = 0


        def dfs(row, col):
            #print(":")

            if row < 0 or col < 0 or row > Rows - 1 or col > Cols - 1 or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dirRow, dirCol in directions:
                dfs(row + dirRow, col + dirCol)

        for i in range(Rows):
            for j in range(Cols):
                if(grid[i][j] == "1"):
                    dfs(i, j)
                    islands += 1

        return islands
        

        