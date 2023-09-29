class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == 'C':
                stack.pop()
            elif ops == 'D':
                stack.append(stack[-1]*2)
            elif ops == '+':
                first = stack.pop()
                second = stack.pop()
                stack.append(second)
                stack.append(first)
                stack.append(first + second)
            else:
                stack.append(int(ops))
        return sum(stack)