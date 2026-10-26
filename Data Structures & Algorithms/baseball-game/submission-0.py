class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for op in operations:
            if op == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                res += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif op == "C":
                rem = stack.pop()
                res -= rem
            else:
                res += int(op)
                stack.append(int(op))
        return res
                
            