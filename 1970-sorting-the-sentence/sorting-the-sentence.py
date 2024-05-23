class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        final = [0] * len(x)
        for i in x:
            final[int(i[-1]) - 1] = i[:len(i) - 1] 
        return " ".join(final)