class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr, tmp = [], []
        prev = nums[0].bit_count()
        for num in nums:
            if num.bit_count() == prev:
                tmp.append(num)
            else:
                arr.extend(sorted(tmp))
                prev = num.bit_count()
                tmp = [num]
        arr.extend(sorted(tmp))
        return sorted(nums) == arr