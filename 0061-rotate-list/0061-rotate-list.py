from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head  # Edge case: No need to rotate

        # Step 1: Find the length of the list
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head  # No need to rotate

        # Step 3: Find the new tail (length - k - 1 node)
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        # Step 4: Rewire the list
        new_head = cur.next  # New head after rotation
        cur.next = None  # Break the connection
        old_tail = new_head
        while old_tail.next:
            old_tail = old_tail.next
        old_tail.next = head  # Connect the old tail to old head

        return new_head
