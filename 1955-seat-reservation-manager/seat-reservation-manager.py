class SeatManager:

    def __init__(self, n: int):
        self.start = [i for i in range(1, n + 1)]
        heapq.heapify(self.start)  

    def reserve(self) -> int:
        return heapq.heappop(self.start)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.start, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)