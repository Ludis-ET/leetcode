class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return k if k <= numOnes else numOnes - max(0, k-numOnes-numZeros)