class Solution(object):
    def smallestEvenMultiple(self, n):
        return n if n % 2 == 0 else n * 2
        