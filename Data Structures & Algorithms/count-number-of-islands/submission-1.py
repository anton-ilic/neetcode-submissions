class Solution:
    def backtrack(self, grid, row, col):
        if not (0 <= row < len(grid)):
            return
        
        if not (0 <= col < len(grid[0])):
            return

        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.backtrack(grid, row + 1, col)
            self.backtrack(grid, row - 1, col)
            self.backtrack(grid, row, col + 1)
            self.backtrack(grid, row, col - 1)
        return


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.backtrack(grid, i, j)
        return count
                
        