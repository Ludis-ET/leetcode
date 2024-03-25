class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        first = 0
        for s in sentences:
            count = 1
            for c in s:
                if c.isspace():
                    count += 1
                if count >= first:
                    first = count
        return first
                
        