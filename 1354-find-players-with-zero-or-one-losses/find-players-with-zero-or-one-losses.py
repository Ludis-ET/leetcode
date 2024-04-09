class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        table = defaultdict(int)
        for w, l in matches:
            table[w] += 0
            table[l] += 1

        winners = [w for w, l in table.items() if l == 0]
        losers = [w for w, l in table.items() if l == 1]
        
        return [sorted(winners), sorted(losers)]