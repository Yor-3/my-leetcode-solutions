# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        def findlen(root):
            count = 0
            last= ListNode(0)
            while root:
                last = root
                count+=1
                root = root.next

            return last,count 
        last,count = findlen(head)
        k = k%count
        if k ==0:
            return head
        cur= head
        for _ in range(k):
            if cur:
                cur =cur.next

        cur2 = head
        prev = None

        while cur:
            cur =cur.next
            prev=cur2
            cur2   = cur2.next

        prev.next =None
        last.next = head
        



        return cur2


