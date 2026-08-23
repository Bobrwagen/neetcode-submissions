class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if not s[-1].isnumeric():
                res = 0
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == "+":
                    res = num1+num2
                elif s == "-":
                    res = num1-num2
                elif s == "*":
                    res = num1*num2
                else:
                    res = int(num1/num2)
                stack.append(res)
            else:
                stack.append(s)
        return stack.pop()
        