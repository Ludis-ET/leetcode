class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        table = defaultdict(int)
        res = float('inf')
        for i, val in enumerate(cards):
            if val in table:
                res = min(res, i - table[val] + 1)
            table[val] = i

        return res if res != float('inf') else -1 
