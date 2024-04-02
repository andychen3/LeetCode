class Solution:
    def simplifyPath(self, path: str) -> str:
        string = path.split("/")
        print(string)
        stack = []
        
        for char in string:
            if char == ".." and stack:
                stack.pop()
            elif char == "." or char == "" or char == "..":
                continue
            else:
                stack.append(char)
        return "/" + "/".join(stack)