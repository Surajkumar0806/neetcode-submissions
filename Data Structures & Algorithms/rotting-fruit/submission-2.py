class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
                        (-1,0),
                        (1,0),
                        (0,-1),
                        (0,1)
                    ]
        fresh = 0
        time = 0
        q = deque([])
        for row in range(len(grid)) :
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh +=1

        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if (new_row in range(len(grid)) 
                        and new_col in range(len(grid[0])) 
                        and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh-=1
            time +=1
        return time if fresh == 0 else -1