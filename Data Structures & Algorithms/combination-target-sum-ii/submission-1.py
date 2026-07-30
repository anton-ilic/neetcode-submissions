class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def permutations(candidates, target, i, current_candidates, current_sum):

            if target == current_sum:
                ans.append(current_candidates)
                return

            elif target < current_sum:
                return
            if i == len(candidates):
                return

            current_candidates_copy = [i for i in current_candidates]
            current_candidates_copy.append(candidates[i])
            permutations(candidates, target, i + 1, current_candidates_copy, current_sum + candidates[i])

            current = candidates[i]
            while i != len(candidates) and current == candidates[i]:
                i += 1
            
            if i == len(candidates):
                return

            permutations(candidates, target, i, current_candidates, current_sum)
            
        permutations(candidates, target, 0, [], 0)
        return ans