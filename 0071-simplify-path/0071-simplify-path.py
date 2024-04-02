class Solution:
    def simplifyPath(self, path: str) -> str:
        string = path.split("/")
        stack = []
        
        for c in string:
            if c == "." or c == "":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "/" + "/".join(stack)