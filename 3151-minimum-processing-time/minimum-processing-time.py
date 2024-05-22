class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        ans = 0
        processorTime.sort()
        tasks.sort(reverse=True)
        j = 0
        for i in processorTime:
            ans = max(ans, i + tasks[j])
            j += 4
        return ans
