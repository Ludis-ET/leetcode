class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                l = stack.pop()
                stack[-1] += max(2 * l, 1)
        return stack.pop()