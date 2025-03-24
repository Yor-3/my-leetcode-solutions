from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        if not len(self.q):
            return -1

        else:
            d = self.q.pop()
        return d
        

    def top(self) -> int:
        if not len(self.q):
            return -1
        else:
            d = self.q[-1]

        return d
        

    def empty(self) -> bool:

        if not len(self.q):
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()