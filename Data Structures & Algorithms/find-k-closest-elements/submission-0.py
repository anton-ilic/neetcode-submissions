class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        differences = {}
        # keep a heap of delta distances to --> and numbers
        # and evict numbers from the bottom
        k_closest = 0
        # if any is closer add it to the min heap
        for num in arr:
            
            if k_closest < k:
                if abs(num - x) not in differences:
                    differences[abs(num - x)] = []
                differences[abs(num - x)].append(num)
                k_closest += 1
            elif abs(num - x) < max(differences.keys()):
                # evict last element in max(num.keys())
                if abs(num - x) not in differences:
                     differences[abs(num - x)] = []
                differences[abs(num - x)].append(num)

                differences[max(differences.keys())].pop()
                if len(differences[max(differences.keys())]) == 0:
                    del differences[max(differences.keys())]
        ans = []
        for key in differences:
            for element in differences[key]:
                ans.append(element)

        return sorted(ans)
