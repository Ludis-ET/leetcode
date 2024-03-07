class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        if len(mountain) <= 2: return []
        return [a for a in range(1,len(mountain) - 1) if mountain[a-1] < mountain[a] > mountain[a+1]]