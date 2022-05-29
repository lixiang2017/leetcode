'''
backtrack
T: O(N * 2^N)
S: O(N)

执行用时：88 ms, 在所有 Python3 提交中击败了26.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了77.30% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        pre_sum = list(accumulate(candidates))
        total = pre_sum[-1]
        used = [False] * n

        def backtrack(path, _sum, i):
            if _sum == target:
                ans.append(path)
                return 
            if i == n:
                return 
            # choose i
            if _sum + candidates[i] <= target:
                if not (i > 0 and candidates[i - 1] == candidates[i] and not used[i - 1]):
                    used[i] = True
                    backtrack(path + [candidates[i]], _sum + candidates[i], i + 1)
                    used[i] = False
            # not choose i
            if total - pre_sum[i] + _sum >= target:
                backtrack(path, _sum, i + 1)

        backtrack([], 0, 0)
        return ans 


'''
倒序，先从较大的数字开始
candidates.sort(reverse=True)

执行用时：48 ms, 在所有 Python3 提交中击败了68.22% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了57.57% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort(reverse=True)
        n = len(candidates)
        pre_sum = list(accumulate(candidates))
        total = pre_sum[-1]
        used = [False] * n

        def backtrack(path, _sum, i):
            if _sum == target:
                ans.append(path)
                return 
            if i == n:
                return 
            # choose i
            if _sum + candidates[i] <= target:
                if not (i > 0 and candidates[i - 1] == candidates[i] and not used[i - 1]):
                    used[i] = True
                    backtrack(path + [candidates[i]], _sum + candidates[i], i + 1)
                    used[i] = False
            # not choose i
            if total - pre_sum[i] + _sum >= target:
                backtrack(path, _sum, i + 1)

        backtrack([], 0, 0)
        return ans 


'''
        if total < target:
            return []
        if total == target:
            return [candidates]

执行用时：52 ms, 在所有 Python3 提交中击败了60.75% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了62.97% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort(reverse=True)
        n = len(candidates)
        pre_sum = list(accumulate(candidates))
        total = pre_sum[-1]
        used = [False] * n
        if total < target:
            return []
        if total == target:
            return [candidates]

        def backtrack(path, _sum, i):
            if _sum == target:
                ans.append(path)
                return 
            if i == n:
                return 
            # choose i
            if _sum + candidates[i] <= target:
                if not (i > 0 and candidates[i - 1] == candidates[i] and not used[i - 1]):
                    used[i] = True
                    backtrack(path + [candidates[i]], _sum + candidates[i], i + 1)
                    used[i] = False
            # not choose i
            if total - pre_sum[i] + _sum >= target:
                backtrack(path, _sum, i + 1)

        backtrack([], 0, 0)
        return ans 


'''
candidates.sort()
if total - pre_sum[i] + _sum >= target and i + 1 < n and candidates[i + 1] <= targ

执行用时：44 ms, 在所有 Python3 提交中击败了81.54% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了33.91% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        pre_sum = list(accumulate(candidates))
        total = pre_sum[-1]
        used = [False] * n
        if total < target:
            return []
        if total == target:
            return [candidates]

        def backtrack(path, _sum, i):
            if _sum == target:
                ans.append(path)
                return 
            if i == n:
                return 
            # choose i
            if _sum + candidates[i] <= target:
                if not (i > 0 and candidates[i - 1] == candidates[i] and not used[i - 1]):
                    used[i] = True
                    backtrack(path + [candidates[i]], _sum + candidates[i], i + 1)
                    used[i] = False
            # not choose i
            if total - pre_sum[i] + _sum >= target and i + 1 < n and candidates[i + 1] <= target - _sum:
                backtrack(path, _sum, i + 1)

        backtrack([], 0, 0)
        return ans 


'''
ans.append(path[:])

执行用时：60 ms, 在所有 Python3 提交中击败了53.62% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.03% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        pre_sum = list(accumulate(candidates))
        total = pre_sum[-1]
        used = [False] * n
        if total < target:
            return []
        if total == target:
            return [candidates]

        def backtrack(path, _sum, i):
            if _sum == target:
                ans.append(path[:])
                return 
            if i == n:
                return 
            # choose i
            if _sum + candidates[i] <= target:
                if not (i > 0 and candidates[i - 1] == candidates[i] and not used[i - 1]):
                    used[i] = True
                    path.append(candidates[i])
                    backtrack(path, _sum + candidates[i], i + 1)
                    path.pop()
                    used[i] = False
            # not choose i
            if total - pre_sum[i] + _sum >= target and i + 1 < n and candidates[i + 1] <= target - _sum:
                backtrack(path, _sum, i + 1)

        backtrack([], 0, 0)
        return ans 


'''
backtrack + freq 

执行用时：84 ms, 在所有 Python3 提交中击败了31.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了25.02% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pos: int, rest: int):
            nonlocal ans, sequence
            if rest == 0:
                ans.append(sequence[:])
                return 
            if pos == len(freq): #  or rest < freq[pos][0]:
                return 
            # not choose freq[pos][0]
            backtrack(pos + 1, rest)
            # choose freq[pos][0], times from 1 to most
            most = min(freq[pos][1], rest // freq[pos][0])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                backtrack(pos + 1, rest - i * freq[pos][0])
            if most:
                sequence = sequence[: -most]

        freq = sorted(Counter(candidates).items())
        ans, sequence = [], []
        backtrack(0, target)
        return ans 


'''
backtrack + freq 

执行用时：48 ms, 在所有 Python3 提交中击败了68.22% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了54.14% 的用户
通过测试用例：175 / 175
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pos: int, rest: int):
            nonlocal ans, sequence
            if rest == 0:
                ans.append(sequence[:])
                return 
            if pos == len(freq) or rest < freq[pos][0]:
                return 
            # not choose freq[pos][0]
            backtrack(pos + 1, rest)
            # choose freq[pos][0], times from 1 to most
            most = min(freq[pos][1], rest // freq[pos][0])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                backtrack(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[: -most]

        freq = sorted(Counter(candidates).items())
        ans, sequence = [], []
        backtrack(0, target)
        return ans 






