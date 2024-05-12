class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, av = 0, sum(arr[:k])
        l, r = 0, k - 1
        while r < len(arr) - 1:
            if av >= threshold * k:
                ans += 1
            av -= arr[l]
            av += arr[r + 1]
            l += 1
            r += 1
        return ans + 1 if av >= threshold * k else ans