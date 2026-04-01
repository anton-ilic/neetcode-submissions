class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # so go from right; 
        best = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = best
            best = max(arr[i], temp)
        return arr
        
