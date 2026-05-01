class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_set = set(allowed)
        for word in words:
            for c in word:
                if c not in allowed_set:
                    count -= 1
                    break
            count += 1

        return count