'''
approach: Hash Table
Time: O(N + N) = O(N)
Space: (N)

执行结果：
通过
显示详情
执行用时：80 ms, 在所有 Python 提交中击败了22.83%的用户
内存消耗：33.5 MB, 在所有 Python 提交中击败了33.69%的用户
'''


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        occurance = defaultdict(int)
        size = len(s)
        for i in range(size - 9):
            occurance[s[i: i + 10]] += 1
        return [substr for substr, count in occurance.iteritems() if count > 1]



'''
执行用时：56 ms, 在所有 Python3 提交中击败了81.01% 的用户
内存消耗：27.8 MB, 在所有 Python3 提交中击败了10.81% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = defaultdict(int)
        for i in range(len(s) - 9):
            c[s[i: i + 10]] += 1
        return [k for k, cnt in c.items() if cnt > 1]

'''
执行用时：68 ms, 在所有 Python3 提交中击败了42.72% 的用户
内存消耗：27.6 MB, 在所有 Python3 提交中击败了34.98% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        ans = []
        c = defaultdict(int)
        for i in range(len(s) - L + 1):
            c[s[i: i + L]] += 1
            if 2 == c[s[i: i + L]]:
                ans.append(s[i: i + L])
        return ans



'''
bitwise + sliding window

执行用时：76 ms, 在所有 Python3 提交中击败了22.52% 的用户
内存消耗：25.1 MB, 在所有 Python3 提交中击败了91.14% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        ans = []
        c = defaultdict(int)
        bins = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        b = 0
        if len(s) <= L:
            return []
        for i in range(L - 1):
            b = (b << 2) | bins[s[i]]

        for i in range(len(s) - L + 1):
            b = ((b << 2) | bins[s[i + L - 1]]) & ((1 << L * 2) - 1)
            c[b] += 1
            if 2 == c[b]:
                ans.append(s[i: i + L])
        return ans


'''
执行用时：136 ms, 在所有 Python3 提交中击败了6.46% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了99.70% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        ans = []
        # c = defaultdict(int)
        c = [0] * (1 << 2 * L)
        bins = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        b = 0
        if len(s) <= L:
            return []
        for i in range(L - 1):
            b = (b << 2) | bins[s[i]]

        for i in range(len(s) - L + 1):
            b = ((b << 2) | bins[s[i + L - 1]]) & ((1 << L * 2) - 1)
            c[b] += 1
            if 2 == c[b]:
                ans.append(s[i: i + L])
        return ans
        