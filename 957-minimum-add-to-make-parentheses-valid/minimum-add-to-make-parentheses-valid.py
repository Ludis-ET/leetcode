class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        val = 0
        for c in s:
            if c == "(":
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                val += 1
        return len(stack) + val
            
        