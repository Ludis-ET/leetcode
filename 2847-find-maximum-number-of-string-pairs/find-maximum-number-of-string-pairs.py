class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen_words, counter = set(), 0
        for word in words:
            if word in seen_words or word[::-1] in seen_words:
                counter += 1
            else:
                seen_words.add(word)
        return counter