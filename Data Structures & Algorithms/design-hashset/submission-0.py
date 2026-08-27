class MyHashSet:

    def __init__(self, max_size = 10000):
        self.store = [[] for i in range(max_size)]
        self.size = max_size

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.store[key % self.size].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            i = self.store[key % self.size].index(key)
            self.store[key % self.size].pop(i)

    def contains(self, key: int) -> bool:
        return key in self.store[key % self.size]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)