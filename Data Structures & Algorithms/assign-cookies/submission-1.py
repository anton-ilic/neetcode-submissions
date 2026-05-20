class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # assuming both g and s r sorted
        g.sort()
        s.sort()
        total = 0
        current = 0
        for c in g:
            if current == len(s):
                return total
            else:
                while current != len(s) and s[current] < c:
                    current += 1

                if current == len(s):
                    return total
                total += 1
                current += 1
        
        return total