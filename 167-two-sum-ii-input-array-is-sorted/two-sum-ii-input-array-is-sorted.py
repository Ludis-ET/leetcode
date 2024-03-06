class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first,last = 0, len(numbers) - 1
        while numbers[first] + numbers[last] != target:
            a, b = numbers[first] , numbers[last]
            if a + b > target:
                last -= 1
            if a + b < target:
                first += 1
        return [first + 1,last + 1]