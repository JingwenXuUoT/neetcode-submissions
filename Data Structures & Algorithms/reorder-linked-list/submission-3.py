# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

         # find the end of the first half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # fast.next for even length list
            # fast for odd length list
        
        # split then reverse the 2^nd half
        second = slow.next
        slow.next = None
        second = self.reverseList(second)
        # the second healf must be the same length or shorter than the first half

        # weave the two halves together
        first = head
        while second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1 # at the termination epoch, this nxt1 is either None or the last one in the first half
            first = nxt1
            second = nxt2
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev