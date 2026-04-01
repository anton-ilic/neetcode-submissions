class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # o (nlogn) ==> square then sort
        squares = {} # num, count
        sol = []

        for i in nums:
            squares[i * i] = squares.get(i * i, 0) + 1

        for elem in sorted(squares.keys()):
            for i in range(0, squares[elem]):
                sol.append(elem)
        return sol