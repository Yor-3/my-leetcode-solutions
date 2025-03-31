class MinStack:


    def __init__(self):
        self.s = []
        

        

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val,min(val,min(val,float('inf')))))
        else:
            self.s.append((val,min(val,self.s[-1][1])))

        

    def pop(self) -> None:
        if not self.s:
            return None
        val,minval = self.s.pop()
        return val
        

    def top(self) -> int:
        if not self.s:
            return None
        return self.s[-1][0]

    def getMin(self) -> int:
        if not self.s:
            return None
        return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()