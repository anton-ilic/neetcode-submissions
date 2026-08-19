class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num // 2 + 1):
            if num == i * i:
                return True
            elif i * i > num:
                return False
        return num == 1