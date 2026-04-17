class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.s) != 1:
            temp.append(self.s.pop(0))
        ans = self.s.pop(0)
        self.s = temp
        return ans
        

    def top(self) -> int:
        temp = []
        while len(self.s) != 1:
            temp.append(self.s.pop(0))
        ans = self.s.pop(0)
        temp.append(ans)
        self.s = temp
        return ans

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()