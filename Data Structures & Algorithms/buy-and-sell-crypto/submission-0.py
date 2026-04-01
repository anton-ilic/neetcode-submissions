class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
                continue
            if buy < price:
                best = max(best, price - buy)

        return best