class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row(board):
            for row in range(0, len(board)):
                seen = set()
                for col in range(0, len(board[0])):
                    if board[row][col] in seen and board[row][col] != ".":
                        return False
                    seen.add(board[row][col])
            return True

        def is_valid_col(board):
            for col in range(0, len(board[0])):
                seen = set()
                for row in range(0, len(board)):
                    if board[row][col] in seen and board[row][col] != ".":
                        return False
                    seen.add(board[row][col])

            return True

        def is_squares_valid(board):
            for offset_row in range(0, 3):
                for offset_col in range(0, 3):
                    if not is_square_valid(board, offset_row, offset_col):
                        return False
            return True
                    
        
        def is_square_valid(board, offset_row, offset_col):
            seen = set()
            for row in range((offset_row - 1) * 3, offset_row * 3):
                for col in range((offset_col - 1) * 3, offset_col * 3):
                    if board[row][col] in seen and board[row][col] != ".":
                        return False
                    seen.add(board[row][col])
            return True



        return is_valid_row(board) and is_valid_col(board) and is_squares_valid(board)

        