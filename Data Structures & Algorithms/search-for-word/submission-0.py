class Solution:
    def search(self, board, word, i, seen, row, col):
        # seen is set of cells that it can't be; ie. (row, col)
        if i == len(word):
            return True

        if row >= len(board) or row < 0:
            return False
    
        if col >= len(board[0]) or col < 0:
            return False
        
        if (row, col) in seen:
            return False

        if board[row][col] == word[i]:
            # go next
            seen_copy = seen.copy()
            seen_copy.add((row, col))
            return self.search(board, word, i + 1, seen_copy, row + 1, col) or self.search(board, word, i + 1, seen_copy, row - 1, col) or self.search(board, word, i + 1, seen_copy, row, col - 1) or self.search(board, word, i + 1, seen_copy, row, col + 1)
        return False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate thru all cells in board; if board[row][col] == word[0] ==>
        for row in range(0, len(board)): 
            for col in range(0, len(board[0])): # o(n**2)
                if board[row][col] == word[0]:
                    if self.search(board, word, 0, set(), row, col):
                        return True
        return False

    # o(n**2) * 4 * n