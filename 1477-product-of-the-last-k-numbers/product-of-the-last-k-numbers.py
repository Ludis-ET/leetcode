class ProductOfNumbers:

    def __init__(self):
        self.product = 1
        self.store = []

    def add(self, num: int) -> None:
        if num:
            self.product *= num
            self.store.append(self.product)
        else:
            self.product = 1
            self.store = []

    def getProduct(self, k: int) -> int:
        if k > len(self.store):
            return 0
        elif k == len(self.store):
            return self.product
        return self.product // self.store[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)