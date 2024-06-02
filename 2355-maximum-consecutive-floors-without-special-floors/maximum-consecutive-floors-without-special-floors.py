class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        l, r = bottom, 0
        ans = 0
        for i in special:
            ans = max(ans, i - l)
            l = i + 1
        ans = max(ans, top - special[-1])
        return ans

