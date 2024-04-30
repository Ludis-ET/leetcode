class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        a = max(arr)
        got = False
        prev = -2
        if len(arr) < 3 or a == arr[-1] or a == arr[0]:
            return False

        for i in arr:
            if (not got and prev >= i) or (got and prev <= i):
                return False
            prev = i
            if i == a: got = True
        return True
