class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        ans, prev = 1, ""
        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != '>':
                ans = max(r - l + 1, ans)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != '<':
                ans = max(r - l + 1, ans)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                prev = ""
        return ans