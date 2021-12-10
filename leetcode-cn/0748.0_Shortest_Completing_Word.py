'''
Hash Table

执行用时：68 ms, 在所有 Python3 提交中击败了23.65% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了59.80% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = [p.lower() for p in licensePlate if p.isalpha()]
        pc = Counter(plate)
        minlen, ans = float('inf'), ''
        for word in words:
            wc = Counter(word)
            if all(wc[p] >= cnt for p, cnt in pc.items()) and len(word) < minlen:
                minlen = len(word)
                ans = word
        return ans


'''
执行用时：124 ms, 在所有 Python3 提交中击败了5.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了79.05% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = Counter(map(str.lower, filter(str.isalpha, licensePlate)))
        return min(filter(lambda w: not (pc - Counter(w)), words) , key=len)
        