# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0,head)
        c1,c2 = d,d

        for _ in range(n+1):
            c1 = c1.next

        while c1:
            c1 =c1.next
            c2 = c2.next

        c2.next = c2.next.next

        return d.next