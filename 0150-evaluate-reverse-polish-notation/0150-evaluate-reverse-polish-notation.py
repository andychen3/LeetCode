class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"-": lambda x,y : x - y, "+": lambda x,y: x + y, "/": lambda x, y: int(x / y), "*": lambda x, y: x * y }

        for token in tokens:
            if token in "-+/*":
                operand1, operand2 = stack.pop(), stack.pop()
                result = operations[token](operand2, operand1)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]