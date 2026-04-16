class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(0, 10):
            if str(i) * 3 in num:
                best = str(i) * 3
        return best