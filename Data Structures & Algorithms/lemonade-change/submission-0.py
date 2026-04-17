class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = {}
        counts[5] = 0
        counts[10] = 0
        for customer in bills:
            if customer == 5:
                counts[5] += 1
            elif customer == 10:
                if counts[5] < 1:
                    return False
                counts[5] -= 1
                counts[10] += 1
            elif customer == 20:
                if counts[10] >= 1 and counts[5] >= 1:
                    counts[10] -= 1
                    counts[5] -= 1
                elif counts[5] >= 3:
                    counts[5] -= 3
                else:
                    return False
        return True