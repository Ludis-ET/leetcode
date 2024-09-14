class SmallestInfiniteSet:

    def __init__(self):
        self.start = 1
        self.remove = set()

    def popSmallest(self) -> int:
        tmp = self.start
        self.remove.add(tmp)
        while self.start in self.remove:
            self.start += 1
        return tmp

    def addBack(self, num: int) -> None:
        if num in self.remove:
            self.remove.remove(num)
        self.start = min(self.start, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)