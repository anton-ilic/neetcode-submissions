class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # find two largest and 2 smallest
        # nums.sort()
        # return nums[-1] * nums[-2] - nums[0] * nums[1]
        largest = - float('inf')
        second_largest = largest

        smallest =  float('inf')
        second_smallest = smallest

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
            
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num
        return largest * second_largest - smallest * second_smallest

