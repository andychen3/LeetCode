class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in "+/-*":
                second_operand = stack.pop()
                first_operand = stack.pop()
                match char:
                    case "+":
                        stack.append(first_operand + second_operand)
                    case "*":
                        stack.append(first_operand * second_operand)
                    case "-":
                        stack.append(first_operand - second_operand)
                    case "/":
                        stack.append(int(first_operand / second_operand))
            else:
                stack.append(int(char))
        return stack[0]