class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0
        directions = {
            (-1, 0),
            (1, 0),
            (0, -1),
            (0,1)
        }

        def dfs(row, col):

            visited.add((row, col))

            for dr, dc in directions:
                new_row = dr + row
                new_col = dc + col

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if (new_row, new_col) not in visited:
                        if grid[new_row][new_col] == "1":
                            dfs(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    island +=1
        return island 