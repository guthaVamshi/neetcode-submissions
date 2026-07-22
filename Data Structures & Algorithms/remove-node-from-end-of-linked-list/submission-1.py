# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Linked List -> List
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        arr.pop(-n)
        dummy = ListNode()
        tail = dummy
        for x in arr:
            tail.next = ListNode(x)
            tail = tail.next
        return dummy.next