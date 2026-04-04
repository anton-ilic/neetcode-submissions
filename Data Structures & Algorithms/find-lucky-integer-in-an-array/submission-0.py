class Solution:
    def findLucky(self, arr: List[int]) -> int:
        keys = {}
        for num in arr:
            keys[num] = keys.get(num, 0) + 1
        
        for key in sorted(keys.keys(), reverse = True):
            if key == keys[key]:
                return key
        return -1