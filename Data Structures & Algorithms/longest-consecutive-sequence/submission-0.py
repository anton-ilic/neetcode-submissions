class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # whenevr u see a element add to a sequence or create a new sequence
        # for each sequence, check if theres a sequence that starts w next element, if so, add it
        seen = set()
        for num in nums:
            seen.add(num)
        
        longest = 0
        
        for num in seen:
            if num - 1 not in seen:
                # start
                c = num + 1
                while c in seen:
                    c += 1
                longest = max(longest, c - num)
        return longest

            