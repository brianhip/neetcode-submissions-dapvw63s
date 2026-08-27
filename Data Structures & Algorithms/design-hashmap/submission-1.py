class MyHashMap:

    def __init__(self, max_size = 1_000_001):
        self.storage = [-1 for i in range(max_size)]
        self.size = max_size

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value

    def get(self, key: int) -> int:
        return self.storage[key]

    def remove(self, key: int) -> None:
        self.storage[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)