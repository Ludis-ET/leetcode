class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for a in range(-1, -len(s)-1, -1):
            if s[a] != " ":
                count += 1
            else:
                if count == 0:
                    continue
                else:
                    break
        return count