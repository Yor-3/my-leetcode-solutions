# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        size = 0

        cur = head
        while cur:
            size+=1
            cur=cur.next
        
        size = size-1

        res = 0
        cur =head
        while cur :
            res += cur.val*(2**size)
            cur=cur.next
            size-=1

        return res