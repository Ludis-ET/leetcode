class Solution:
    def minimumSteps(self, s: str) -> int:
        ans, zero = 0, 0
        for i in s[::-1]:
            zero += i == '0'
            if i == '1':
                ans += zero
        return ans