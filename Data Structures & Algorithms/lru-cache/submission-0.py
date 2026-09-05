class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # my biggest stuggles are the way to handle edge cases
    # writing one shared helper for "unlink a node" and one for  "insert a node at head" removes almost every edge cases checks, since each operation only needs to reason about one side at a time instead of by hand every time

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUMap = {} # key and node address
        # dummy head/tail sentinels - real most-recent sits right after head, real least-recent sits before tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node):
        # self.head is a dummy node
        # node should be inserted right after it
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        
    def get(self, key: int) -> int:
        # use hashmap for O(1) get
        # use a doubly-linked list to maintain the order of the LRU
        # the node of the linkedlist is key,value pair
        # the least recently used node at the head, the most recently used node at the tail
        # IMPORTANT: the map and the list must be modified together
        if key in self.LRUMap:
            node = self.LRUMap[key]
            # update the order
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # edge case: if key already exist, should update its value then update its address
        if key in self.LRUMap:
            self._remove(self.LRUMap[key])
        node = Node(key, value)
        self.LRUMap[key] = node
        self._insert_at_front(node)
        if len(self.LRUMap) > self.capacity:
            # remove the node at real tail
            # self.tail is a dummy tail
            tail = self.tail.prev # need to explicitly store this node
            # otherwise, after _remove, the real tail is no longer this node
            self._remove(tail)
            del self.LRUMap[tail.key]

        
