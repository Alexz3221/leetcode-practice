# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
  
        while head is not None:
            next_node = head.next  # Save the remaining list
            head.next = previous   # Reverse this link
            previous = head        # Move previous forward
            head = next_node       # Move head forward
  
        return previous

