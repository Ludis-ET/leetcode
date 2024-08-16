class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mx, mn, ans = arrays[0][-1], arrays[0][0], 0
        for i in range(1, len(arrays)):
            el = arrays[i]
            ans = max(ans, el[-1] - mn, mx - el[0])
            mx = max(mx, el[-1])
            mn = min(mn, el[0])
        return ans