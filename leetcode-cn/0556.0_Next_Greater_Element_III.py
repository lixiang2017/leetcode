'''
approach: Greedy
intuition: next permutation
Time: O(N + N) = O(N)
Space: O(N)

执行用时：24 ms, 在所有 Python 提交中击败了23.33%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.67%的用户
'''


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int, str(n))
        N = len(digits)
        pos = -1  # position
        for i in range(N - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pos = i
                break
        
        if -1 == pos:
            return -1
        else:
            greaterIdx = self.findGreaterIdx(digits, N, pos)
            digits[pos], digits[greaterIdx] = digits[greaterIdx], digits[pos]
            rearrange = digits[: i + 1] + digits[i + 1: ][:: -1]
            rearrange = int(''.join(map(str, rearrange)))
            if rearrange > (1 << 31) - 1 or rearrange < 1:
                return -1
            else:
                return rearrange

    def findGreaterIdx(self, digits, N, pos):
        for i in range(N - 1, pos, -1):
            if digits[i] > digits[pos]:
                return i


'''
执行用时：5180 ms, 在所有 Python3 提交中击败了5.66% 的用户
内存消耗：189.6 MB, 在所有 Python3 提交中击败了5.47% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = tuple(str(n))
        ss = sorted(s)
        # ps = list(permutations(ss))  # wrong for 11
        ps = sorted(set(permutations(ss)))
        idx = ps.index(s)
        if idx == -1 or idx == len(ps) - 1:
            return -1
        nxt = ps[idx + 1]
        ans = int(''.join(nxt))
        if ans <= (1 << 31) - 1:
            return ans 
        return -1


'''
next permutation

执行用时：36 ms, 在所有 Python3 提交中击败了66.42% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.06% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        L = len(s)
        if 1 == L:
            return -1
        i = L - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
        if -1 == i:
            return -1 
        # find index j, s[j] just larger than s[i]
        j = i + 1
        while j < L and s[j] > s[i]:
            j += 1
        j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1: ] = s[i + 1: ][:: -1]

        ans = int(''.join(s))
        if ans <= (1 << 31) - 1:
            return ans 
        return -1




