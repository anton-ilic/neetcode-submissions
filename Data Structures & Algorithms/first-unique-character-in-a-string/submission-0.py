class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        seen_map = {}
        for i in range(0, len(s)):
            current = s[i]
            if current in seen:
                if current in seen_map:
                    del seen_map[current] 
                continue
            seen.add(current)
            seen_map[current] = i
            
        if len(seen_map) == 0:
            return -1
        return min(seen_map.values())


                