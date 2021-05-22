'''
approach: Greedy + Sort + Two Pointers
Time: O(MlogM + NlogN + M + N) =  O(MlogM + NlogN),
 M is the number of children and N si the number of cookies.
Space: O(1)

执行结果：通过
显示详情
执行用时：40 ms, 在所有 Python 提交中击败了85.33%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了57.27%的用户
'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = j = content = 0
        children, cookies = len(g), len(s)
        while i < children and j < cookies:
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content




'''
approach: Greedy + Sort + Two Pointers
Time: O(MlogM + NlogN + M + N) =  O(MlogM + NlogN),
 M is the number of children and N si the number of cookies.
Space: O(1)

执行用时：68 ms, 在所有 Python3 提交中击败了54.05% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了60.63% 的用户
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children, cookies = len(g), len(s)
        i = j = content = 0
        while i < children and j < cookies:
            while j < cookies and s[j] < g[i]:
                j += 1
            if j < cookies and s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                break

        return content
