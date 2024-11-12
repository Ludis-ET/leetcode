class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx
