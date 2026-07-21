# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        valset = set()
        prev , current = None,head
        while current:
            if current not in valset:
                valset.add(current)
                current = current.next
            else:
                return True
        return False


        