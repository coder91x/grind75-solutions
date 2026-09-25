lass Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        previous_mru = self.right.prev

        previous_mru.next = node
        node.prev = previous_mru
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value

            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.hmap[key] = node
            self.insert(node)

            if len(self.hmap) > self.capacity:
                lru = self.left.next

                self.remove(lru)
                del self.hmap[lru.key]
