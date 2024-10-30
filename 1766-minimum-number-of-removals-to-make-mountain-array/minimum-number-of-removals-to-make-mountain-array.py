class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        leftDP, rightDP = [1] * len(nums), [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    leftDP[i] = max(leftDP[i], leftDP[j] + 1)
                    
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    rightDP[i] = max(rightDP[i], rightDP[j] + 1)
                    
        ans = 0
        for i in range(len(nums)):
            
            if (leftDP[i] != 1 and rightDP[i] != 1):
                ans = max(ans, leftDP[i] + rightDP[i])
                
        return len(nums) - ans + 1