class Solution:
    def ispair(self,a,b):
        if a=='(' and b==')' or a=='[' and b==']' or a=='{' and b=='}':
            return True
        return False
    def isValid(self, s: str) -> bool:
        stack=[0]*len(s)
        open=['(','{','[']
        close=[')','}',']']
        top=-1
        for i in s:
            if i in open:
                top+=1
                stack[top]=i
            elif i in close:
                if not self.ispair(stack[top],i):
                    return False
                top-=1
        if top == -1:
            return True
        return False