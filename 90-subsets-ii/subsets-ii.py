class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def back(i, cur):
            if i >= len(nums):
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            back(i + 1, cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            back(i + 1, cur)
        back(0, [])
        return ans