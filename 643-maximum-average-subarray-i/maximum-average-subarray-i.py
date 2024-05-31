class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == k:
            return sum(nums) / n
        f, s = 0, k
        summ = sum(nums[:k])
        maxx = summ / k
        while s < n:
            summ -= nums[f]
            summ += nums[s]
            maxx = max(maxx, summ / k)
            f += 1
            s += 1
        return maxx