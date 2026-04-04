class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq = {}
        for key in counts.keys():
            count = counts[key]
            if count not in freq:
                freq[count] = []
            freq[count].append(key)

        sol = []
        for count in sorted(freq.keys()):
            elements = freq[count]
            for element in sorted(elements, reverse = True):
                for _ in range(0, count):
                    sol.append(element)
        return sol