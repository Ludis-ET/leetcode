class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, stack, x = [], [], 0
        for i in s:
            if not stack and i == '(':
                stack.append(i)
            elif i == '(' or (i == ')' and x > 0):
                ans.append(i)
                x += 1 if i == '(' else -1
            elif stack:
                stack.pop()
        return ''.join(ans)
