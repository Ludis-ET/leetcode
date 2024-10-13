class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr, mx = [], float('-inf')
        for i in nums:
            heapq.heappush(arr, [i[0], 0, i])
            mx = max(mx, i[0])

        ans, check = None, float('inf')
        while arr:
            mn, i, lst = heapq.heappop(arr)
            i += 1

            if mx - mn < check:
                ans = [mn, mx]
                check = mx - mn

            if i < len(lst):
                mn = lst[i]
                mx = max(mx, mn)
                heapq.heappush(arr, [mn, i, lst])
            else: break
        return ans