class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        for i in range(2, n):
            arr = [arr[1], arr[0] + arr[1]]
        return sum(arr) if n > 1 else n