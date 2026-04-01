class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1 
        
        # element : counts
        counts_list = []
        for elem in counts:
            count = counts[elem]
            counts_list.append((elem, count))
        
        counts_list.sort(key = lambda counts_list : counts_list[1], reverse = True)
        
        ans = []
        for i in range(0, k):
            ans.append(counts_list[i][0])
        return ans
        