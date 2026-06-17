class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # since all nums r distinct, can just use backtracking
        ans = []
        end = len(nums)
        def traverse(nums, i, target_sum, current_sum, current_nums):
            if current_sum == target_sum:
                ans.append(current_nums)
                return 
            elif current_sum > target_sum: # no -ives
                return

            if i == end:
                return 
            
            # either 1. add and continue, 2. add and don't continue, 3. don't add and cont
            traverse(nums, i + 1, target_sum, current_sum, current_nums)
            current_nums_copy = current_nums.copy()
            current_nums_copy.append(nums[i])
            traverse(nums, i, target_sum, current_sum + nums[i], current_nums_copy)
        traverse(nums, 0, target, 0, [])
        return ans
            
            
