class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        table = defaultdict(int)
        ans = float('-inf')

        cur, l = 0, 0
        for r in range(len(nums)):
            cur += nums[r]
            table[nums[r]] += 1
            if r - l + 1 == k:
                if len(table) == r - l + 1:
                    ans = max(ans, cur)
                if table[nums[l]] == 1:
                    del table[nums[l]]
                else:
                    table[nums[l]] -= 1
                cur -= nums[l]
                l += 1
        return max(ans, 0)
            