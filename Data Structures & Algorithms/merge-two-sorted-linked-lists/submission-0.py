# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        head = temp
        heap = []
        # min heap; 
        i = 0
        if list1:
            heapq.heappush(heap, (list1.val, i, list1))

        if list2:
            i += 1
            heapq.heappush(heap, (list2.val, i, list2))
        while len(heap) != 0:
            current = heapq.heappop(heap)[2]
            temp.next = current
            temp = temp.next
            if current.next:
                i += 1
                heapq.heappush(heap, (current.next.val, i, current.next))
        return head.next