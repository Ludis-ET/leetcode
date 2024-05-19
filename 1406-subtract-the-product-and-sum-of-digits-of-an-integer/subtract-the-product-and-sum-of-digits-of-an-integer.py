class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sm, mu = 0, 1
        while n > 0:
            sm += n % 10
            mu *= n % 10
            n //= 10
        return mu - sm