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

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def enqueue(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if self.hash.get(key):
            node = self.hash[key]

            self.remove(node)
            self.enqueue(node)

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

            self.remove(node)
            self.enqueue(node)
            
        else:
            node = Node(key, value)
            self.hash[key] = node

            self.enqueue(node)

        # remove
        if len(self.hash) > self.capacity:
            node = self.head.next
            self.remove(node)

            del self.hash[node.key]






