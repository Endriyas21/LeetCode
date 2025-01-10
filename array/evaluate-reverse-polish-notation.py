class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif n == '-':
                a, b == int(stack.pop()), int(stack.pop())
                stack.append(b-a)
            elif n == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif n == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(n)
        return stack[-1]