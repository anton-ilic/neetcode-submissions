class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # at most 15 matchsticks; can use backtracking to check all combinations
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse = True)
        def backtrack(matchsticks, one, two, three, four, i):
            if i == len(matchsticks):
                return one == two == three == four

            if one > target or two > target or three > target or four > target:
                return False
            
            return backtrack(matchsticks, one + matchsticks[i], two, three, four, i + 1) or backtrack(matchsticks, one, two + matchsticks[i], three, four, i + 1) or backtrack(matchsticks, one, two, three + matchsticks[i], four, i + 1) or backtrack(matchsticks, one, two, three, four + matchsticks[i], i + 1)
        
        return backtrack(matchsticks, 0, 0, 0, 0, 0)