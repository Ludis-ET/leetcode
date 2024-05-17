class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        f = 0
        prefix = []
        for i in nums:
            prefix.append(f + i)
            f += i
        
        before = 0
        for i in range(len(nums)):
            after = prefix[-1] - prefix[i]
            if before == after:
                return i
            before += nums[i] 
        return -1