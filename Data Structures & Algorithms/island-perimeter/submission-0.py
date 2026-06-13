class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 0:
                    continue 

                if y == 0:
                    peri += 1
                elif grid[y - 1][x] == 0:
                    peri += 1
                
                if y == len(grid) - 1:
                    peri += 1
                elif grid[y + 1][x] == 0:
                    peri += 1


                if x == 0:
                    peri += 1
                elif grid[y][x - 1] == 0:
                    peri += 1
                
                if x == len(grid[0]) - 1:
                    peri += 1
                elif grid[y][x + 1] == 0:
                    peri += 1
        return peri