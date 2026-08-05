class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        island = 0 

        def dfs(row, col):
            if (row < 0 or col < 0 or
                row >= len(grid) or col >= len(grid[0])
                or grid[row][col] == "0"):
                return 
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row+dr, col+dc)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    island +=1
        return island