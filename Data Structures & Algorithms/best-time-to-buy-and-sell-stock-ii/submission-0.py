class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        total = 0
        for i in prices:
            if i > buy:
                total += i - buy
            buy = i
        return total

        