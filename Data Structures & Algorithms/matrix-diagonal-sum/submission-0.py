class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        end = len(mat)

        total = 0
        for i in range(0, end):
            total += mat[i][i]
            mat[i][i] = 0
        
        for j in range(0, end):
            total += mat[j][end - 1]
            end -= 1
        return total