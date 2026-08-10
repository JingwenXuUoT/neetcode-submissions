# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return None
        # this is not needed

        # Find the nth node by slow, fast pointer
        dummy = ListNode(0, head) # avoid the removed node is the head node
        # dummy also handles empty and single-node input without a special case.
        slow = fast = dummy
        for _ in range(n+1):
            # not range(n)
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        # after while loop, slow lands on the node befoer the target
        
        slow.next = slow.next.next
        # breaking the connection by slow.next = None is not necessary, because if nothing points to a node, then python automatically collects it.

        return dummy.next

        