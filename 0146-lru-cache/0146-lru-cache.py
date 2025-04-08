class Node:
    def __init__(self,key,val):
        self.key,self.val  = key,val
        self.prev,self.next = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache ={}

        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev =self.right,self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def remove(self,node):
        prev,nex = node.prev,node.next
        prev.next = nex
        nex.prev =prev

    def insert(self,node):
        prev,nex = self.right.prev,self.right

        prev.next,node.prev =node,prev
        node.next,nex.prev = nex,node  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)