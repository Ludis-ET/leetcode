class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = track = 0
        for a in gain:
            track += a
            highest = max(highest, track)
        return highest