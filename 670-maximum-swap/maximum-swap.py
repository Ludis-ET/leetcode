class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [i for i in str(num)]
        def mx(i):
            mx = [int(num[i]), i]
            for i in range(i + 1, len(num)):
                if int(num[i]) >= mx[0]:
                    mx = [int(num[i]), i]
            return mx

        for i in range(len(num)):
            if i + 1 < len(num):
                n, j = mx(i + 1)
                if n > int(num[i]):
                    num[i], num[j] = num[j], num[i]
                    return int(''.join(num))
        return int(''.join(num))