'''
Hash Table + Sort

执行用时：52 ms, 在所有 Python3 提交中击败了74.33% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了51.00% 的用户
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        freqs = [(ch, freq) for ch, freq in cnt.items()]
        freqs.sort(key = lambda t: -t[1])
        return ''.join(ch * freq for ch, freq in freqs)
