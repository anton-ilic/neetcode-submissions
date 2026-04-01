class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(0, n):
        #     nums1[m + i] = nums2[i]
        # nums1 = nums1.sort()

        insert_position = m + n - 1
        first_candidate = m - 1
        second_candidate = n - 1
        while insert_position >= 0:
            if first_candidate < 0:
                nums1[insert_position] = nums2[second_candidate]
                second_candidate -= 1
            elif second_candidate < 0:
                nums1[insert_position] = nums1[first_candidate]
                first_candidate -= 1
            elif nums1[first_candidate] > nums2[second_candidate]:
                nums1[insert_position] = nums1[first_candidate]
                first_candidate -= 1
            else:
                nums1[insert_position] = nums2[second_candidate]
                second_candidate -= 1
            insert_position -= 1 
        
        


