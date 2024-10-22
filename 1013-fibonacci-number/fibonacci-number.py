class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        for i in range(n - 2):
            arr[0], arr[1] = arr[1], arr[0] + arr[1]
        return arr[0] + arr[1] if n > 1 else n