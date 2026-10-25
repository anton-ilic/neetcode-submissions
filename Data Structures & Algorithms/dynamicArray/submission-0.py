class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.current = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.current == self.capacity:
            self.resize()

        self.arr[self.current] = n
        self.current += 1

    def popback(self) -> int:
        self.current -= 1
        return self.arr[self.current]

    def resize(self) -> None:
        new_arr = [None] * (self.capacity * 2)
        for i in range(0, len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.current
    
    def getCapacity(self) -> int:
        return self.capacity
