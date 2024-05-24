class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path.split("/"))
        stack = []
        for i in path.split("/"):
            if len(i) > 0:
                if i == ".." and len(stack) > 0:
                    stack.pop()
                elif i != "." and i != "..":
                    stack.append(i)
        return "/" + "/".join(stack)