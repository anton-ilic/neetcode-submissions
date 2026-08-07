# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        # node to remove is the count - nth 
        to_remove = count - n
        # ie. if to_remove is 0 ==> remove head
        if to_remove == 0:
            return head.next

        temp = head
        for _ in range(to_remove - 1):
            temp = temp.next
        
        temp.next = temp.next.next
        return head
            
