class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        large = 0 
        count = 0
        for i, x in enumerate(flips, 1):
            large = max(large, x)
            if i == large:
                count += 1
        return count