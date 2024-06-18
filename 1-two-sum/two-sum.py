class Solution(object):
    def twoSum(self, nums, target):
        ans = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in ans:
                return [ans[temp], i]
            ans[nums[i]] = i
        return []
