'''
Accepted
'''
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split()
        count = 0
        
        def check(word):
            for ch in word:
                if ch in broken:
                    return False
            return True
        
        for word in words:
            if check(word):
                count += 1
        
        return count
        