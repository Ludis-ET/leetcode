class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = defaultdict(int)
        symbols = "!?',;."
        for i in symbols:
            paragraph = paragraph.replace(i, " ")

        for a in paragraph.split():
            a = a.lower()
            if a not in banned:
                words[a] += 1

        high = max(words.values())
        for key, value in words.items():
            if value == high:
                return key