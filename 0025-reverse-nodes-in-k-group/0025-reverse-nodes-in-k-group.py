# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur =head

        for _ in range(k):
            if not cur:
                return head

            cur =cur.next

        prev,cur =None,head

        for _ in range(k):
            nex =cur.next
            cur.next= prev
            prev= cur
            cur =nex

        head.next = self.reverseKGroup(cur,k)

        return prev