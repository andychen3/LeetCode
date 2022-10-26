class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        print(path.split('/'))
        
        for c in path.split('/'):
            if c == '..':
                if stack:
                    stack.pop()
                continue
            elif c == '.' or not c:
                continue
            stack.append(c)
            
        return '/'+'/'.join(stack)
