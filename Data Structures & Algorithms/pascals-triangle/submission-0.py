class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1]]
        if numRows == 1:
            return sol

        sol.append([1, 1])
        if numRows == 2:
            return sol
        
        for row in range(3, numRows + 1):
            current = []
            current.append(1)
            for end in range(0, len(sol[-1]) - 1):
                current.append(sol[-1][end] + sol[-1][end + 1])

            current.append(1)
            sol.append(current) 
        return sol