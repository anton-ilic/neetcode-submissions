class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # best = ""
        # for i in range(0, 10):
        #     if str(i) * 3 in num:
        #         best = str(i) * 3
        # return best
        best = ""
        for i in range(1, len(num) - 1):
            if num[i] == num[ i - 1] == num[i + 1]:
                if best == "":
                    best = num[i] * 3
                elif int(best[0]) < int(num[i]):
                    best = num[i] * 3
        return best