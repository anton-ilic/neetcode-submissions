class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # count those characters; input them; if NOT them append
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        ans = []
        for c in order:
            if c in counts:
                for _ in range(0, counts[c]):
                    ans.append(c)
                del counts[c]
        
        for c in counts.keys():
            for _ in range(0, counts[c]):
                ans.append(c)
        return ''.join(ans)
            