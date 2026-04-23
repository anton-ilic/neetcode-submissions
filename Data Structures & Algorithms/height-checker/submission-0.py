class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_expected = sorted(heights)
        cnt = 0
        for i in range(0, len(heights)):
            if heights[i] != heights_expected[i]:
                cnt += 1
        return cnt