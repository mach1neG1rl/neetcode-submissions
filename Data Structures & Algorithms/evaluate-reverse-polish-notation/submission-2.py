class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                lastNum = int(stack.pop())
                stack[-1] = int(stack[-1])
                if i == "+":
                    stack[-1] += lastNum
                elif i == "-":
                    stack[-1] -= lastNum
                elif i == "*":
                    stack[-1] *= lastNum
                elif i == "/":
                    stack[-1] /= lastNum
            else:
                stack.append(i)
        
        return int(stack[-1])