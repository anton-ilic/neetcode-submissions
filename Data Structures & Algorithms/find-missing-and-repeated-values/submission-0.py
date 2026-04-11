class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans = []
        for element in grid:
            for matrixElement in element:
                if matrixElement in seen:
                    ans.append(matrixElement)
                seen.add(matrixElement)
        
        for i in range(1, len(grid) * len(grid) + 1):
            if i not in seen:
                ans.append(i)
                return ans
        return ans