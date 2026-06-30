class ListNode():
    def __init__(self, val):
        self.val = val
        self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if current == None:
                return -1
            current = current.next_node
        if not current:
            return -1
        return current.val

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = ListNode(val)
        self.head.next_node = temp

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        
        current = self.head
        while current.next_node:
            current = current.next_node
        
        current.next_node = ListNode(val)
        

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head == None:
                return False
            self.head = self.head.next_node
            return True
        
        prev = self.head
        current = self.head
        for _ in range(index):
            if current == None:
                return False
            prev = current
            current = current.next_node

        if not current:
            return False
        else:
            prev.next_node = current.next_node
        return True

    def getValues(self) -> List[int]:
        temp = self.head
        ans = []
        while temp:
            ans.append(temp.val)
            temp = temp.next_node
        
        return ans
