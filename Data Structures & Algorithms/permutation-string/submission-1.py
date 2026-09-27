class Solution:
    def checkInclusionHelper(self, counts_s1, counts_s2):
        # check that counts_s2 includes s1
        for key in counts_s1.keys():
            if counts_s1[key] > counts_s2.get(key, 0):
                return False
        return True # this window does include

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check if perm(s1) in s2
        if len(s2) < len(s1):
            return False
        
        # otherwise iterate
        characters_s1 = {}
        characters_s2 = {}

        for c in s1:
            characters_s1[c] = characters_s1.get(c, 0) + 1

        low = 0
        for current in range(0, len(s2)):
            characters_s2[s2[current]] = characters_s2.get(s2[current], 0) + 1
            # add this character

            # current window is too long; increase
            while current - low + 1 > len(s1):
                # remove character from window
                characters_s2[s2[low]] = characters_s2.get(s2[low], 0) - 1
                low += 1
            
            # current window contains the substring
            if current - low + 1 == len(s1) and self.checkInclusionHelper(characters_s1, characters_s2):
                return True

        return False