'''
执行结果：
超出时间限制
最后执行的输入：
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
查看全部
43 / 44 个通过测试用例

Time: O(N ^ 2)
Space: O(N ^ 2)
'''

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        N = len(a)
        b = [1] * N
        for i in range(N):
            b[i] = functools.reduce(lambda x, y: x * y, [a[j] for j in range(N) if j != i])
        return b

'''
approach: Iteration / Dynamic Programming
Time: O(N + N) = O(N)
Space: O(N ^ 2)

执行结果：
通过
显示详情
执行用时：60 ms, 在所有 Python 提交中击败了71.95%的用户
内存消耗：27 MB, 在所有 Python 提交中击败了60.57%的用户
'''

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        N = len(a)
        b = [1] * N
        c = d = 1
        for i in range(1, N):
            c *= a[i - 1]
            b[i] = c

        for j in range(N - 2, -1, -1):
            d *= a[j + 1]
            b[j] *= d

        return b

'''
approach: Iteration / Dynamic Programming
only one pass
Time: O(N)
Space: O(N ^ 2)

执行用时：68 ms, 在所有 Python 提交中击败了44.31%的用户
内存消耗：27.2 MB, 在所有 Python 提交中击败了33.33%的用户
'''


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        N = len(a)
        b = [1] * N
        c = d = 1
        for i in range(0, N):
            b[i] *= c
            c *= a[i]

            b[N - i - 1] *= d
            d *= a[N - i - 1]

        return b
        