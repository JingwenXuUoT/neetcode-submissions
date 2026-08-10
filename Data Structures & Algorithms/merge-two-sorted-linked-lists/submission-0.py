# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-100)
        itr = dummy_node

        l1 = list1
        l2 = list2

        while l1 and l2:
            if(l1.val < l2.val):
                itr.next = l1
                l1 = l1.next
            else:
                itr.next = l2
                l2 = l2.next
            itr = itr.next

        if l1:
            itr.next = l1
        elif l2:
            itr.next = l2

        return dummy_node.next
        