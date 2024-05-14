class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix, j = [], 0
        for i in nums:
            prefix.append(j + i)
            j += i

        ans = []
        l, m = 0, 0
        for r in range(len(nums)):
            if r - l + 1 > k and r + k < len(nums):
                total = prefix[r + k] - m
                ans.append(total//(k + k + 1))
                m += nums[l]
                l += 1
            else:
                ans.append(-1)
        return ans