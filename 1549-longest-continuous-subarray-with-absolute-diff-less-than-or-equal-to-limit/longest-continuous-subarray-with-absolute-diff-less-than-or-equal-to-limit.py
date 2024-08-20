class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mnq, mxq = deque(), deque()
        ans, l = 0, 0 
        for r in range(len(nums)):
            while mnq and nums[mnq[-1]] > nums[r]:
                mnq.pop()
            while mxq and nums[mxq[-1]] < nums[r]:
                mxq.pop()
            mnq.append(r)
            mxq.append(r)
            while l < len(nums) and abs(nums[mnq[0]] - nums[mxq[0]]) > limit:
                l += 1
                if mnq[0] < l:
                    mnq.popleft()
                if mxq[0] < l:
                    mxq.popleft()
            ans = max(ans, r - l + 1)
        return ans