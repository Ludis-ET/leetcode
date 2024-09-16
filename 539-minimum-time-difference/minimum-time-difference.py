class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        mins = []
        for i in range(len(time)):
            t = time[i]
            mins.append((int(t[:2]) * 60) + int(t[3:]))
        mins.sort()
        ans = float('inf')
        for i in range(1, len(mins)):
            ans = min(ans, mins[i] - mins[i - 1])
        tmp = ((24 * 60) - mins[-1]) + mins[0]
        return min(ans, tmp)