class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        for i in self.hashset:
            if i == key:
                return 
        self.hashset.append(key) 
        return

    def remove(self, key: int) -> None:
        for i in range(0, len(self.hashset)):
            if self.hashset[i] == key:
                self.hashset.pop(i)
                return
        return 
        

    def contains(self, key: int) -> bool:
        for i in self.hashset:
            if i == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)