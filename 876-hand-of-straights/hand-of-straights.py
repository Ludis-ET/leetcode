class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)

        for i in sorted(cnt):
            v = cnt[i]
            if v > 0:
                for j in range(i, i + groupSize):
                    cnt[j] -= v
                    if cnt[j] < 0:
                        return False
        return True