class Solution:
    def minimumLength(self, s: str) -> int:
        pre, suf = 0, len(s) - 1
        
        while pre < suf and s[pre] == s[suf]:
            char = s[pre]
            while pre <= suf and s[pre] == char:
                pre += 1
            while suf >= pre and s[suf] == char:
                suf -= 1
        
        return suf - pre + 1