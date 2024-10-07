class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        myHash = {"B" : "A", "D" : "C"}
        for c in s:
            if stack and myHash.get(c, 0) == stack[-1]:
                stack.pop()  
            else:
                stack.append(c)
        return len(stack)