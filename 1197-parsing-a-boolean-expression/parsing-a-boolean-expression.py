class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in expression:
            if i == ')':
                tmp = ""
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack.pop()
                ex = stack.pop()
                ans = True if tmp[0] == 't' else False
                for j in tmp.split(','):
                    j = True if j == 't' else False
                    if ex == '|':
                        ans |= j
                    elif ex == '&':
                        ans &= j
                    else:
                        ans = not ans
                stack.append('t' if ans else 'f')
            else:
                stack.append(i)
        return True if stack[0] == 't' else False