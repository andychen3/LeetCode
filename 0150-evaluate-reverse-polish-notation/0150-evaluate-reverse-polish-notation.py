class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char in '+-*/':
                second = stack.pop()
                first = stack.pop()
                if char is '+':
                    stack.append(first+second)
                elif char is '-':
                    stack.append(first-second)
                elif char is '*':
                    stack.append(first*second)
                elif char is '/':
                    stack.append(int(first/second))
            else:
                stack.append(int(char))
                
        return stack[-1]
                
                
            