class MinStack:

    def __init__(self):
        self.stck = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

    def pop(self) -> None:
        if len(self.mins) == 0:
            raise ValueError("empty stack")
        self.stck.pop()
        self.mins.pop()

    def top(self) -> int:
        if len(self.mins) == 0:
            raise ValueError("empty stack")
        return self.stck[-1]
        

    def getMin(self) -> int:
        if len(self.mins) == 0:
            raise ValueError("empty stack")
        return self.mins[-1]