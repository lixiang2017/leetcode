'''
执行用时：76 ms, 在所有 Python3 提交中击败了55.45% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了47.27% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(word):
            c = Counter(word)
            for ch in string.ascii_lowercase:
                if ch in c:
                    return c[ch]
        
        fs = [f(word) for word in words]
        fs.sort()
        n = len(fs)
        
        return [n - bisect_right(fs, f(q)) for q in queries]
        