class Node:
    def __init__(self, key: int, val: int, next: Node = None, prev: Node = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

    def get(self, key: int) -> int:
        if self.hash.get(key):
            node = self.hash[key]

            node.prev.next = node.next
            node.next.prev = node.prev


            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            node.next = self.tail

            return self.hash[key].val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        # init
        if len(self.hash) == 0:
            new = Node(key, value)
            self.hash[key] = new
            new.prev = self.head
            new.next = self.tail
            self.head.next = new
            self.tail.prev = new
            return

        # std operation
        if self.hash.get(key):
            node = self.hash[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev


            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            node.next = self.tail
            
        else:
            node = Node(key, value)
            self.hash[key] = node

            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            node.next = self.tail

        # remove
        if len(self.hash) > self.capacity:
            node = self.head.next
            
            node.prev.next = node.next
            node.next.prev = node.prev

            del self.hash[node.key]






