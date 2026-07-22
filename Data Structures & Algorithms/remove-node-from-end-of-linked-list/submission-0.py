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

        # Remove value 3
        arr.pop(-n)

        # List -> Linked List
        dummy = ListNode(0)
        current = dummy

        for x in arr:
            current.next = ListNode(x)
            current = current.next

        return dummy.next