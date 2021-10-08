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
        