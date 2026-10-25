class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # bruteforce: try every window size; check counts vs k
        # 1. we need to have window with n - k characters of one type;
        low = 0
        best = 0
        counts = {}
        for high in range(0, len(s)):
            counts[s[high]] = counts.get(s[high], 0) + 1
            if len(counts) != 0:
                # while window invalid; shrink
                while high - low + 1 - max(counts.values()) > k:
                    counts[s[low]] = counts[s[low]] - 1
                    low += 1
            best = max(best, high - low + 1)
        return best