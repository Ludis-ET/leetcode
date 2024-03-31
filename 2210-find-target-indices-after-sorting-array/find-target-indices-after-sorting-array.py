class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if a == target:
                ans.append(i)
        return ans