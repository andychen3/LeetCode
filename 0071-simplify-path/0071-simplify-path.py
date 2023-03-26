class Solution:
    def simplifyPath(self, path: str) -> str:
        converted_path = path.split("/")
        stack = []
        
        for c in converted_path:
            if c == "..":
                if stack:
                    stack.pop()
            elif c == "" or c == ".":
                continue
            else:
                stack.append(c)
                
        return "/" + "/".join(stack)