class Solution:
    def minLength(self, s: str) -> int:
        ans=[]
        for char in s:
            if ans and (ans[-1]=='A' and char=='B' or ans[-1]=='C' and char=='D'):
                ans.pop()
            else:
                ans.append(char)
        return len(ans)                