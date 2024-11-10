class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        ans, cur = float('inf'), nums[0]
        l = 0
        for r in range(len(nums)):
            cur |= nums[r]
            for i in range(32):
                bits[i] += (1 if nums[r] & 1 << i != 0 else 0)
                
            while cur >= k and l <= r:
                ans = min(ans, r - l + 1)
                cur = 0
                for i in range(32):
                    bits[i] = max(0, bits[i] - (1 if nums[l] & 1 << i != 0 else 0))
                    if bits[i] > 0:
                        cur |= 1 << i
                l += 1
        return ans if ans != float('inf') else -1