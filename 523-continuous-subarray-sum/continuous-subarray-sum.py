class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        table = {0 : -1}
        total = 0
        for i, x in enumerate(nums):
            total += x
            r = total % k
            if r not in table:
                table[r] = i
            elif i - table[r] > 1:
                return True
        return False





