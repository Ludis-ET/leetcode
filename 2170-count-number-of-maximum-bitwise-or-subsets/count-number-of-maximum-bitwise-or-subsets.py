class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for i in nums:
            mx |= i
            
        def backtrack(i, cur):
            nonlocal mx
            if i == len(nums):
                return 1 if cur == mx else 0
            return (backtrack(i + 1, cur | nums[i]) + backtrack(i + 1, cur))
        return backtrack(0, 0)