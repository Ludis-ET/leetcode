class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wend = set(dictionary)
        ans = []
        for i in sentence.split():
            for j in range(len(i) + 1):
                x = i[:j]
                if x in wend:
                    ans.append(x)
                    break
            else:
                ans.append(i)
        return " ".join(ans)
