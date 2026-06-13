class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # bruteforce: iterate thru rows, then columns
        count = 0
        # on row iter; store if server; add if so

        # iterating thru columns
        for row in range(0, len(grid)):
            # grid[row][col]
            seen = set() # of seen Col values
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1 or grid[row][col] == 2:
                    seen.add(col)

            if len(seen) > 1:
                for element_col in seen:
                    if grid[row][element_col] == 1:
                        grid[row][element_col] = 2
                        count += 1

        # iterate thru col
        for col in range(0, len(grid[0])):
            seen = set() # of seen Col values
            for row in range(0, len(grid)):
                if grid[row][col] == 1 or grid[row][col] == 2:
                    seen.add(row)

            if len(seen) > 1:
                for row in seen:
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        count += 1

        return count

