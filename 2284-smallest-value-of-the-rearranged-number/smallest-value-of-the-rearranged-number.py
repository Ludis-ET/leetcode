class Solution:
    def smallestNumber(self, num: int) -> int:
        x = str(num)
        if num >= 0:
            x = sorted(x)
            if x[0] != "0":
                return int("".join(x))
            y = [0,0]
            for i in range(len(x)):
                if x[i] != "0":
                    y[0] = x[i]
                    y[1] = i
                    break
            x[0] = y[0]
            x[y[1]] = "0"
            return int("".join(x))
        else:
            return -int("".join(sorted(x[1:], reverse=True)))