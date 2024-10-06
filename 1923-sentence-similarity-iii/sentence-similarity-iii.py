class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        l, r = 0, 0
        
        while l < len(words2) and words1[l] == words2[l]:
            l += 1
        
        while r < len(words2) and words1[-(r + 1)] == words2[-(r + 1)]:
            r += 1
        
        return l + r >= len(words2)
