# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None or head is None:
            return None

        if head.next.next is None:
            head.next =None
            return head

        slow =fast =  head
        dummy= ListNode(0,head)
        prev = dummy

        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

            if fast is None:
                break

        prev.next = slow.next
        slow.next = None

        return dummy.next
                