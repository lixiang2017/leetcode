class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def weight(word: str) -> int:
            return sum(weights[ord(c) - ord('a')] for c in word) % 26
        
        m = {i: chr(ord('a') + 25 - i) for i in range(26)}
        s = ''.join(m[weight(word)] for word in words)
        return s
