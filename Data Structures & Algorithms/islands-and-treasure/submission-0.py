class Solution:
    def expandOutward(self, grid, row, col, current_distance):
        
        # boundry check
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        # if the current one is -1; return
        if grid[row][col] == -1:
            return
        
        if grid[row][col] < current_distance: # if closer treasure, return 
            return

        grid[row][col] = current_distance
        self.expandOutward(grid, row + 1, col, current_distance + 1)
        self.expandOutward(grid, row - 1, col, current_distance + 1)
        self.expandOutward(grid, row, col + 1, current_distance + 1)
        self.expandOutward(grid, row, col - 1, current_distance + 1)



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 0:
                    # expand outward from 0; 
                    self.expandOutward(grid, row, col, 0)


