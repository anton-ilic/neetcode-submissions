class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        ans = 0
        for key in counts.keys():
            if counts[key] > 1:
                total = 0
                for i in range(0, counts[key]):
                    total += i
                ans += total
        return ans