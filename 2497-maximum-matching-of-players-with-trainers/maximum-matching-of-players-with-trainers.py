class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l, r = 0, 0
        counter = 0
        while r < len(trainers) and l < len(players):
            if players[l] <= trainers[r]:
                counter += 1
                l += 1
                r += 1
            else:
                r += 1
        return counter