class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): # let str1 always be the longer
            str1, str2 = str2, str1

        largest = ""
        for i in range(0, len(str1)):
            if str1[0:i + 1] * (len(str2) // (i + 1)) == str2 and str1[0:i + 1] * (len(str1) // (i + 1)) == str1:
                largest = str1[0:i + 1]
        return largest