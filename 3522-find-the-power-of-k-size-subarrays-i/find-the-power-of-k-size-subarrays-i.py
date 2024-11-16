class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans, haset = [], set()
        l, defect = 0, 0
        for r in range(len(nums)):
            if r > 0 and k > 1 and nums[r - 1] != nums[r] - 1:
                defect += 1
                haset.add(r - 1)
                
            if r - l + 1 == k:
                ans.append(nums[r] if not defect else -1)
                defect -= l in haset
                l += 1
        return ans