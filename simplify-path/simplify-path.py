class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        
        for c in path.split('/'):
            if c == '..':
                if stack:
                    stack.pop()
            elif c != '.' and c:
                stack.append(c)
            
        return '/'+'/'.join(stack)
