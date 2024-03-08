class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for a in range(1,n + 1):
            if a % 3 == 0 and a % 5 == 0: ans.append("FizzBuzz")
            elif a % 5 == 0: ans.append("Buzz")
            elif a % 3 == 0: ans.append("Fizz")
            else: ans.append(str(a))
        return ans
        