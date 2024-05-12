class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        ans = 0
        for i in ["T","F"]:
            count = 0
            l = 0
            for r in range(n):
                if answerKey[r] != i:
                    count += 1
                while count > k:
                    if answerKey[l] != i:
                        count -= 1
                    l += 1
                ans = max(ans, r - l + 1)
        return ans