'''
approach: Sort
Time: O(MlogM + MlogM * (N-M) ), where M is the length of s1 and N is the length of s2.
Space: O(1)

执行结果：通过
显示详情
执行用时：5224 ms, 在所有 Python 提交中击败了13.27%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了5.10%的用户
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1, s2 = list(s1), list(s2)
        size1, size2 = len(s1), len(s2)
        s1.sort()
        for i in range(size2 - size1 + 1):
            part = s2[i: i + size1]
            part.sort()
            if part == s1:
                return True
        return False


'''
sliding window
T: O(M + 26 * (N - M))
S: O(26 * 2)

执行用时：52 ms, 在所有 Python3 提交中击败了98.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了91.92% 的用户
通过测试用例：107 / 107
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = [ord(ch) - ord('a') for ch in s1]
        b = [ord(ch) - ord('a') for ch in s2]
        target, window = [0] * 26, [0] * 26
        m, n = len(a), len(b)
        if m > n:
            return False 
        for x, y in zip(a, b):
            target[x] += 1
            window[y] += 1
        if target == window:
            return True 
        for i in range(m, n):
            window[b[i]] += 1
            window[b[i - m]] -= 1
            if target == window:
                return True 
        return False 


'''
sliding window
T: O(M + N + 26)
S: O(26)

执行用时：60 ms, 在所有 Python3 提交中击败了90.47% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了84.15% 的用户
通过测试用例：107 / 107
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        diff, diff_cnt = [0] * 26, 0
        if m > n:
            return False 
        for ch1, ch2 in zip(s1, s2):
            diff[ord(ch1) - ord('a')] -= 1
            diff[ord(ch2) - ord('a')] += 1
        diff_cnt = sum(d != 0 for d in diff)
        if 0 == diff_cnt:
            return True 
        for i in range(m, n):
            d2 = ord(s2[i]) - ord('a')
            d1 = ord(s2[i - m]) - ord('a')
            if d1 == d2:
                continue 
            if diff[d2] == 0:
                diff_cnt += 1
            diff[d2] += 1
            if diff[d2] == 0:
                diff_cnt -= 1            

            if diff[d1] == 0:
                diff_cnt += 1
            diff[d1] -= 1
            if diff[d1] == 0:
                diff_cnt -= 1              

            if diff_cnt == 0:
                return True 
        return False 




