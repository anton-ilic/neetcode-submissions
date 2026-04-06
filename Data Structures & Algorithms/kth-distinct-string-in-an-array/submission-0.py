class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # hashmap is in order of seen; therefore, the kth string w count == 1 is the kth distinct
        counts = {}
        for elem in arr:
            counts[elem] = counts.get(elem, 0) + 1
        
        count = 1
        for key in counts:
            if counts[key] == 1 and count == k:
                return key
            elif counts[key] == 1:
                count += 1
        return ""

