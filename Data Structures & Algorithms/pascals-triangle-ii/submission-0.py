class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # there r rowIndex elements
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        ans = [1, 1]
        for row in range(1, rowIndex + 1):
            current = []
            current.append(1)
            for i in range(1, row):
                current.append(ans[i - 1] + ans[i])
            current.append(1)
            ans = current
        return ans