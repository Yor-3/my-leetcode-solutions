# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = []
        if headA is None:
            return None
        cur = headA

        while cur:
            s.append(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in s:
                return cur

            cur = cur.next

        return None
