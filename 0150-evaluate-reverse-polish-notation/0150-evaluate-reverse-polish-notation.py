class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in tokens:
            if i  not in operators:
                stack.append(i)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == '+':
                    res = int(num2) +int(num1)
                if i == '-':
                    res = int(num2) -int(num1)
                if i == '*':
                    res = int(num1) * int(num2)

                if i == '/':
                    res = int(num2)/int(num1)

                stack.append(int(res))

        return int(stack[0])
