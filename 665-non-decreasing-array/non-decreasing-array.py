class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        first = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if first:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                first = True

        return True
