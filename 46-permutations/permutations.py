class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        prev = self.permute(nums[1:])
        ans = []
        for n in prev:
            for i in range(len(n) + 1):
                tmp = n.copy()
                tmp.insert(i, nums[0])
                ans.append(tmp)
        return ans