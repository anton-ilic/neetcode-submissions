class Solution:
    def minOperations(self, s: str) -> int:
        # first chr can be a 1 or a 0

        changes_first = 0
        changes_second = 0
        for i in range(0, len(s)):
            # first[i] % 2 == 0 should be 0
            # first[i] % 2 == 1 should be 1

            # second[i] % 2 == 0 should be 1
            # second[i] % 2 == 1 should be 0
            if i % 2 == 0:
                if s[i] == "0":
                    pass
                elif s[i] == "1":
                    changes_first += 1

                if s[i] == "0":
                    changes_second += 1
                elif s[i] == "1":
                    pass


            elif i % 2 == 1:
                
                if s[i] == "0":
                    changes_first += 1
                elif s[i] == "1":
                    pass

                if s[i] == "0":
                    pass
                elif s[i] == "1":
                    changes_second += 1
        return min(changes_first, changes_second)