class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        rev = nums[::-1]

        for i in range(len(nums) - 1):
            pre[i + 1] = pre[i] * nums[i]
            suf[i + 1] = suf[i] * rev[i]

        rev = suf[::-1]

        return [pre[i] * rev[i] for i in range(len(nums))]

        