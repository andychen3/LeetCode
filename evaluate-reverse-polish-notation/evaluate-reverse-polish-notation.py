class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in '+*-/':
                second_num = stack.pop()
                first_num = stack.pop()
                if token == '+':    
                    stack.append(first_num+second_num)
                elif token == '*':
                    stack.append(first_num*second_num)
                elif token == '-':
                    stack.append(first_num-second_num)
                elif token =='/':
                    stack.append(int(first_num/second_num))
            else:
                stack.append(int(token))
        return stack.pop()
        
        
        
#         stack = []
#         operations ={'+': lambda a,b: a+b, '*':lambda a, b: a*b, '-':lambda a,b: a-b, '/':lambda a,b: int(a/b)}
        
#         for num in tokens:
#             if num in operations:
#                 operation = operations[num]
#                 first = stack.pop()
#                 second = stack.pop()
#                 stack.append(operation(second,first))
#             else:
#                 stack.append(int(num))
#         return stack.pop()