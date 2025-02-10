# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,start,end):
        prev, cur = None,start
        while cur!=end:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count , temp = 0,head
        while temp and count<k:
            temp = temp.next
            count+=1
        if count<k: return head

        newhead=self.reverse(head,temp)
        head.next=self.reverseKGroup(temp,k)
        return newhead
        