class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def flatten_helper(node):
            curr = node
            last = None
            
            while curr:
                if curr.child:
                    child = curr.child
                    curr.child = None
                    child_tail = flatten_helper(child)
                    next_node = curr.next
                    curr.next = child
                    child.prev = curr
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    last = child_tail
                else:
                    last = curr
                
                curr = curr.next
            
            return last
        
        flatten_helper(head)
        return head
