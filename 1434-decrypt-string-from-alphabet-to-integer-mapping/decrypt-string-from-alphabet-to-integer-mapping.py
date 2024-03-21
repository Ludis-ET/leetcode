class Solution(object):
    def freqAlphabets(self, s):
        alp = [chr(i) for i in range(ord('a'), ord('j') + 1)] + \
              [chr(i) for i in range(ord('k'), ord('z') + 1)]
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                letter = s[i-2:i]
                ans = alp[int(letter) - 1] + ans
                i -= 3
            else:
                letter = s[i]
                ans = alp[int(letter) - 1] + ans
                i -= 1
        return ans
