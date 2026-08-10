# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast pointer
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
    # while loop terminates: if fast runs off the end, the list is finite and there's no cycle. The if inside handles detection, list has cycle will be terminiated by the detection. while fast and fast.next also covers the empty list, i.e. head = None, the while loop never runs

        return False