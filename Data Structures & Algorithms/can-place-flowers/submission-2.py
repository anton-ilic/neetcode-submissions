class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # greedy
        total = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            return n == 0
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            total += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                total += 1
        
        if flowerbed[- 1] == 0 and flowerbed[- 2] == 0:
            total += 1

        return total >= n
