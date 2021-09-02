'''
T: O(N + M)
S: O(N + M)

执行用时：32 ms, 在所有 Python3 提交中击败了74.56% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了61.59% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()
        
        for revision1, revision2 in zip(v1, v2):
            if revision1 < revision2:
                return -1
            elif revision1 > revision2:
                return 1
        
        L1, L2 = len(v1), len(v2)
        if L1 < L2:
            return -1
        elif L1 > L2:
            return 1
        else:
            return 0

'''
T: O(N + M)
S: O(N + M)

执行用时：28 ms, 在所有 Python3 提交中击败了90.99% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了37.67% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            r1, r2 = int(v1), int(v2)
            if r1 != r2:
                return 1 if r1 > r2 else -1
        return 0

'''
Simulation, Two Pointers
T: O(N + M)
S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了90.99% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.32% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        N, M = len(version1), len(version2)
        i = j = 0
        while i < N or j < M:
            x = 0
            while i < N and version1[i] != '.':
                x = x * 10 + ord(version1[i]) - ord('0')
                i += 1
            i += 1  # to skip '.'
            y = 0
            while j < M and version2[j] != '.':
                y = y * 10 + ord(version2[j]) - ord('0')
                j += 1
            j += 1 # to skip '.'
            if x != y:
                return 1 if x > y else -1
        return 0
