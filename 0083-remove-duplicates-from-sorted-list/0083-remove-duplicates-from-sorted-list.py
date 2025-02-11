from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head  # Pointer to current node
        
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next  # Skip the duplicate
            else:
                cur = cur.next  # Move to next distinct element

        return head  # Return modified list
