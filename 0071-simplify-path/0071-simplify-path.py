class Solution:
    def simplifyPath(self, path: str) -> str:
        abs_path = path.split("/")
        print(abs_path)
        stack = []

        for c in abs_path:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        print("/".join(stack))

        return "/" + "/".join(stack)
            