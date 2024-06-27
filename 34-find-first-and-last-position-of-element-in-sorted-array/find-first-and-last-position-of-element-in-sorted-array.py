class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target, tmp):
            l, r, i = 0, len(nums) - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if tmp:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        left = bs(nums, target, True)
        right = bs(nums, target, False)
        
        return [left, right]
            