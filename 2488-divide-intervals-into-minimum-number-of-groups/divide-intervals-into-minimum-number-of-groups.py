class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse=True)
        ans = []
        while intervals:
            add = intervals.pop()
            if ans and ans[0] < add[0]:
                tmp = heapq.heappop(ans)
            heapq.heappush(ans, add[1])
        return len(ans)