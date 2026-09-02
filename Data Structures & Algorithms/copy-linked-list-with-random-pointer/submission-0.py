"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # maintain a oldNode to newNode mapping, deduplication
        if not head:
            return None

        old_to_new = {}

        # pass 1: create every clone, register in map
        # because random can point to a node later in the list that hasn't been cloned yet. When cur's clone is being built, old_to_new[cur.random] might not exist yet if cur.random comes after cur. The standard fix is two passes: first pass creates every clone (so the map is fully populated), second pass wires next and random, since by then every lookup is guaranteed to succeed.
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # pass 2: wire next and random, translating through the map
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]
