'''
brute force
hash table
T: O(50 * 2^10 * 10 + 50 * 2^10 * 50) = 3 * 10^6

我为啥铁憨憨去枚举所有子序列了呢

执行用时：712 ms, 在所有 Python3 提交中击败了5.47% 的用户
内存消耗：19.9 MB, 在所有 Python3 提交中击败了5.47% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n = len(strs)
        # for every str, defaultdict(set)
        # len of subseq -> set of subseq
        subseq = [defaultdict(set) for _ in range(n)]
        max_l = 0
        for i, s in enumerate(strs):
            L = len(s)
            max_l = max(max_l, L)
            for state in range(1, 1 << L):
                sub = ''.join(s[j] if state >> j & 1 else '' for j in range(L))
                subseq[i][len(sub)].add(sub)

        for L in range(max_l, 0, -1):
            for i in range(n):
                if L not in subseq[i]:
                    continue
                for cand in subseq[i][L]:
                    if not any( cand in subseq[j][L] for j in chain(range(i), range(i + 1, n)) ):
                        return L 
        return -1 


'''
ref:
https://leetcode.cn/submissions/detail/329681235/

如果subsequence满足条件，那其父串肯定也满足条件啊。
所以，不用管每一个串的子序列，只考虑每一个原始串即可。
所以，原始串之间相互比较即可。原始串之间检查是否是子序列。

执行用时：52 ms, 在所有 Python3 提交中击败了18.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.52% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSequence(longer: str, shorter: str) -> bool:
            it = iter(longer)
            return all(need in it for need in shorter)
        
        for cur in sorted(strs, key=len, reverse=True):
            if 1 == sum(isSubSequence(other, cur) for other in strs):
                return len(cur)
        return -1 


'''
执行用时：44 ms, 在所有 Python3 提交中击败了35.82% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了93.53% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSequence(longer: str, shorter: str) -> bool:
            if len(longer) < len(shorter):
                return False
            it = iter(longer)
            return all(need in it for need in shorter)
        
        for cur in sorted(strs, key=len, reverse=True):
            if 1 == sum(isSubSequence(other, cur) for other in strs):
                return len(cur)
        return -1 


'''
T: O(50*log50 + 50*50*10)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了35.82% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.64% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSequence(longer: str, shorter: str) -> bool:
            # check if shorter isSubSequence of longer
            if len(longer) < len(shorter):
                return False
            m, n, i, j = len(longer), len(shorter), 0, 0
            while i < m and j < n:
                if longer[i] == shorter[j]:
                    j += 1
                i += 1
            return j == n
        
        for cur in sorted(strs, key=len, reverse=True):
            if 1 == sum(isSubSequence(other, cur) for other in strs):
                return len(cur)
        return -1

'''
执行用时：52 ms, 在所有 Python3 提交中击败了18.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.60% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSequence(longer: str, shorter: str) -> bool:
            # check if shorter isSubSequence of longer
            if len(longer) < len(shorter):
                return False
            m, n, i, j = len(longer), len(shorter), 0, 0
            while i < m and j < n:
                if longer[i] == shorter[j]:
                    j += 1
                i += 1
            return j == n
        
        ans = -1
        for i, cur in enumerate(strs):
            check = True
            for j, other in enumerate(strs):
                if i != j and isSubSequence(other, cur):
                    check = False
                    break
            if check:
                ans = max(ans, len(cur))
        return ans 



'''
使用状态转移方程计算最长公共子序列的长度，时间空间复杂度都会高一些
T: O(50 * 50 * 10 * 10)
S: O(10 * 10)

执行用时：336 ms, 在所有 Python3 提交中击败了5.47% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.62% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubSequence(longer: str, shorter: str) -> bool:
            # check if shorter isSubSequence of longer
            m, n  = len(longer), len(shorter)
            if m < n:
                return False
            f = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    f[i][j] = f[i - 1][j - 1] + bool(longer[i - 1] == shorter[j - 1])
                    f[i][j] = max(f[i][j], f[i - 1][j])
                    f[i][j] = max(f[i][j], f[i][j - 1])
            return f[m][n] == n 
             
        ans = -1
        for i, cur in enumerate(strs):
            check = True
            for j, other in enumerate(strs):
                if i != j and isSubSequence(other, cur):
                    check = False
                    break
            if check:
                ans = max(ans, len(cur))
        return ans 





