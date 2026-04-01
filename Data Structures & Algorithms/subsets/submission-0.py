class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        curr = []
        def bfs(i):
            if i == len(nums):
                sol.append(curr.copy())
                return
            curr.append(nums[i])
            bfs(i + 1)
            curr.pop()
            bfs(i + 1)
        bfs(0)
        return sol