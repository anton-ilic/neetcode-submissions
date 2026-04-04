class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greaters = {} # ELEMENT, NEXT

        elems = [] # greater elements
        for i in range(len(nums2) - 1, -1, -1):
            current = nums2[i]
            if len(elems) != 0:
                next_greaters[current] = -1
                while len(elems) != 0:
                    posibility = elems[-1]
                    if posibility > current:
                        next_greaters[current] = posibility
                        break
                    else:
                        elems.pop()
            else:
                next_greaters[current] = -1

            elems.append(current)

        
        ans = []
        # since all integers are unique; just check hashmap and replace values w it 
        for num in nums1:
            ans.append(next_greaters[num])

        return ans