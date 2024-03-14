class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = self.countAndSay(n - 1)
        ans = ""
        ans, count = "", 1
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
            else:
                ans += str(count) + s[i]
                count = 1
        return ans