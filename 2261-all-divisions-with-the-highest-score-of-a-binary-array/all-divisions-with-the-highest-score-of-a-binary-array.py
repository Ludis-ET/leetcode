class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        suf = nums[::-1]
        for i in range(n):
            prefix[i + 1] = prefix[i] + (nums[i] == 0)
            suffix[i + 1] = suffix[i] + (nums[n - 1 - i] == 1)

        mx = 0
        ans = []
        for i in range(n + 1):
            x = prefix[i] + suffix[n - i]
            if x > mx:
                mx = x
                ans = [i]
            elif x == mx:
                ans.append(i)
        return ans

        