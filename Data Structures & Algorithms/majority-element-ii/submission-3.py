class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = 0
        a_count = 0
        b = 0
        b_count = 0
        for i in nums:
            if i == a:
                a_count += 1
            elif i == b:
                b_count += 1
            else:
                if a_count <= 0:
                    a = i
                    a_count = 1
                    # b_count -= 1
                elif b_count <= 0:
                    b = i
                    b_count = 1
                    # a_count -= 1
                else:
                    a_count -= 1
                    b_count -= 1
        a_count = 0
        b_count = 0
        for i in nums:
            if i == a:
                a_count += 1
            elif i == b:
                b_count += 1
        if a_count > len(nums) // 3 and b_count > len(nums) // 3:
            return [a, b]
        elif a_count > len(nums) // 3:
            return [a]
        elif b_count > len(nums) // 3:
            return [b]
        return []

