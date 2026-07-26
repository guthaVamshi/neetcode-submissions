# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1_val = l1.val if l1 else 0
            v2_val = l2.val if l2 else 0
            sum_digit = v1_val + v2_val + carry
            carry = sum_digit //10
            digit = sum_digit % 10
            tail.next = ListNode(digit)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        