class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.val = val
            self.key= key

            self.prev = self.next= None
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addNode(self,newnode):
        temp = self.head.next
        newnode.next = temp 
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    def deleteNode(self,delnode):
        pre = delnode.prev
        nex = delnode.next
        pre.next = nex
        nex.prev = pre

    
        

    def get(self, key: int) -> int:
        if key in self.m:
            res = self.m[key]
            ans = res.val
            del self.m[key]
            self.deleteNode(res)
            self.addNode(res)
            self.m[key] = self.head.next
            return ans

        return -1


        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            cur = self.m[key]
            del self.m[key]
            self.deleteNode(cur)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key,value))
        self.m[key] =self.head.next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)