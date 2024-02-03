class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in "+-*/":
                second = stack.pop()
                first = stack.pop()
                match char:
                    case "+":
                        stack.append(first + second)
                    case "-":
                        stack.append(first - second)
                    case "*":
                        stack.append(first * second)
                    case "/":
                        stack.append(int(first / second))
            else:
                stack.append(int(char))
        return stack[0]