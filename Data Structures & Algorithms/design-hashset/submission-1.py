class MyHashSet:

    def __init__(self):
        self.data = [-1] * 10000

    def probe(self, key: int, i: int) -> int:
        return self.data[(key + i ** 2) % 10000]

    def add(self, key: int) -> None:
        i = 0
        while self.probe(key, i) != key and self.probe(key, i) != -1 and self.probe(key, i) != -2:
            i += 1

        if self.probe(key, i) != key:
            self.data[(key + i ** 2) % 10000] = key
        
    def remove(self, key: int) -> None:
        i = 0
        while self.probe(key, i) != key and self.probe(key, i) != -1:
            i += 1
        
        if self.probe(key, i) == key:
            self.data[(key + i ** 2) % 10000] = -2

    def contains(self, key: int) -> bool:
        i = 0
        while self.probe(key, i) != key and self.probe(key, i) != -1:
            i += 1
        
        return self.probe(key, i) == key
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)