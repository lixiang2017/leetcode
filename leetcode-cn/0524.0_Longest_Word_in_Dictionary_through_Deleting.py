'''
custom sort + two pointers

执行用时：336 ms, 在所有 Python3 提交中击败了62.71% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了7.40% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def compare(x, y):
            if len(x) < len(y):
                return 1
            elif len(x) > len(y):
                return -1
            else:
                if x < y:
                    return -1
                else:
                    return 1

        dictionary.sort(key= cmp_to_key(compare))
        for d in dictionary:
            if self.isSubSeq(s, d):
                return d
        return ''
    
    def isSubSeq(self, s, d):
        L1, L2 = len(s), len(d)
        i = j = 0
        while i < L1 and j < L2:
            if s[i] == d[j]:
                i += 1; j += 1
            else:
                i += 1
        return j == L2

'''
输入：
"abce"
["abe","abc"]
输出：
"abe"
预期结果：
"abc"
'''

