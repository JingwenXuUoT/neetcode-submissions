# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode(-1)
        cur_sum_node = res

        while l1 or l2 or carry:
            # need to include carry in the conditioning, only until all the three are None or 0 could the loop be terminated
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            cur_sum = val1 + val2 + carry
            carry = cur_sum // 10
            remain = cur_sum % 10

            cur_sum_node.next = ListNode(remain)
            # in process, only need to create new nodes for remain
            # carry will be added in the next iteration to the next remain
            cur_sum_node = cur_sum_node.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return res.next
