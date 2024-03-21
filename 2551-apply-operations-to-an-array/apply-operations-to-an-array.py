class Solution(object):
    def applyOperations(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
        c,a=0,[]
        for i in nums:
            if i==0:
                c+=1
                continue
            a.append(i)
        return a+[0]*c

        