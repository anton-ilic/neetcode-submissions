class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort by free

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = {}
        for num in counts: # number, count
            if counts[num] not in buckets:
                buckets[counts[num]] = []
            buckets[counts[num]].append(num)

        sol = []
        for i in range(max(buckets.keys()), -1, -1):
            if i in buckets:
                for j in buckets[i]:
                    if len(sol) == k:
                        return sol
                    sol.append(j)
            if len(sol) == k:
                return sol
        return sol
        