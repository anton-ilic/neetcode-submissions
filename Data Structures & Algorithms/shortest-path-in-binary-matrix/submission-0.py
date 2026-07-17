class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ans = float("inf")

        def _is_valid(row, col):
            return (
                0 <= row < len(grid)
                and 0 <= col < len(grid[0])
            )

        def _is_end(row, col):
            return row == len(grid) - 1 and col == len(grid[0]) - 1

        def shortestPath(current_grid, row, col, moves):
            nonlocal ans

            if not _is_valid(row, col):
                return

            if current_grid[row][col] == 1:
                return

            if moves >= ans:
                return

            if _is_end(row, col):
                ans = min(ans, moves)
                return

            # Deep-copy every row
            new_grid = [current_row[:] for current_row in current_grid]
            new_grid[row][col] = 1

            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1),
            ]

            for row_change, col_change in directions:
                shortestPath(
                    new_grid,
                    row + row_change,
                    col + col_change,
                    moves + 1,
                )

        shortestPath(grid, 0, 0, 1)

        return -1 if ans == float("inf") else ans
        