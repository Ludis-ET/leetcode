class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        hp = []
        pas = 0
        for r, trip in enumerate(trips):
            pa, s, e = trip
            pas += pa

            while hp and s >= hp[0][0]:
                pas -= heapq.heappop(hp)[1]
            
            heapq.heappush(hp, (e, pa))
            if pas > capacity:
                return False
        return True