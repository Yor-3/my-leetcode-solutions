class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char is not "]":
                stack.append(char)
            else:
                sub_str = ""
                while stack[-1] is not "[":
                    sub_str = stack.pop()+sub_str

                stack.pop()

                multi = ""
                while stack and stack[-1].isdigit():
                    multi = stack.pop()+multi

                stack.append(int(multi)*sub_str)

        return "".join(stack)