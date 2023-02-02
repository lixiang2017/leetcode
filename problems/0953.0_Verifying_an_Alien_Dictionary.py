'''
Runtime: 49 ms, faster than 31.23% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 13.8 MB, less than 77.66% of Python3 online submissions for Verifying an Alien Dictionary.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict(zip(order, string.ascii_lowercase))
        seq = [''.join(mapping.get(ch) for ch in word) for word in words]
        return seq == sorted(seq)

'''
Runtime: 52 ms, faster than 28.04% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 13.8 MB, less than 99.16% of Python3 online submissions for Verifying an Alien Dictionary.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda word: [order.index(char) for char in word])

'''
Runtime: 47 ms, faster than 35.69% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 14 MB, less than 31.27% of Python3 online submissions for Verifying an Alien Dictionary.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict(zip(order, string.ascii_lowercase))
        prev = ''
        for word in words:
            trans = ''.join(map(mapping.__getitem__, word))
            if prev > trans:
                return False
            prev = trans
        return True
    
'''
Runtime: 41 ms, faster than 58.29% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 13.8 MB, less than 77.66% of Python3 online submissions for Verifying an Alien Dictionary.


Your input
["ubg","kwh"]
"qcipyamwvdjtesbghlorufnkzx"
stdout

### mapping
{113: 97, 99: 98, 105: 99, 112: 100, 121: 101, 97: 102, 109: 103, 119: 104, 118: 105, 100: 106, 106: 107, 116: 108, 101: 109, 115: 110, 98: 111, 103: 112, 104: 113, 108: 114, 111: 115, 114: 116, 117: 117, 102: 118, 110: 119, 107: 120, 122: 121, 120: 122}

['uop', 'xhq']
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = str.maketrans(order, string.ascii_lowercase)
        prev = ''
        for w in words:
            trans = w.translate(mapping)
            if prev > trans:
                return False
            prev = trans 
        return True

