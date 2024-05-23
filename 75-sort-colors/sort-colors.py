class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = defaultdict(int)
        for i in nums:
            table[i] += 1
            
        for i in range(table[0]):
            nums[i] = 0
        
        for j in range(table[0],table[0] + table[1]):
            nums[j] = 1

        for k in range(table[0] + table[1], table[0] + table[1] + table[2]):
            nums[k] = 2
        