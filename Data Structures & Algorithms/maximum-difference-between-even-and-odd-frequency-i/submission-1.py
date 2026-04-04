class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        min_odd = float('inf'); max_odd = 0
        min_even = float('inf'); max_even = 0;
        for key in counts:
            if counts[key] % 2 != 0:
                max_odd = max(max_odd, counts[key])
                min_odd = min(min_odd, counts[key])
            else:
                min_even = min(min_even, counts[key])
                max_even = max(max_even, counts[key])
        return max_odd - min_even