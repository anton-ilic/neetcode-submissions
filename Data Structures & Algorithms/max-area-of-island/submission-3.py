class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        
        best = 0
        def dfs(row, col):
            if (row < 0 or col < 0):
                return 0
            
            if (row >= len(grid) or col >= len(grid[0])):
                return 0
            
            if grid[row][col] == 0:
                return 0

            if (row, col) in seen:
                return 0

            seen.add((row, col))
            
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
    
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    best = max(best, dfs(row, col))

        return best

