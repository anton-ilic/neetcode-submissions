class Solution:
    def iterate_on_point(self, row, col, grid):
        if row < 0 or col < 0:
            return 0
        
        if row >= len(grid) or col >= len(grid[0]):
            return 0
        
        if grid[row][col] == 0:
            return 0

        grid[row][col] = 0
        return 1 + self.iterate_on_point(row, col + 1, grid) + self.iterate_on_point(row, col - 1, grid) + self.iterate_on_point(row - 1, col, grid) + self.iterate_on_point(row + 1, col, grid)
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # so we find a 1 and turn all adjacents to 
        best = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    # You may assume all four edges of the grid are surrounded by water.
                    total = self.iterate_on_point(row, col, grid)

                    best = max(best, total)
                
        return best