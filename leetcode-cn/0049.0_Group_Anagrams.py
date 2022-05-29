'''
要用 k = tuple(sorted(Counter(s).items()))
不能用 k = tuple(sorted(Counter(s))), 这种只计算了key, 忽略了cnt 

执行用时：104 ms, 在所有 Python3 提交中击败了8.27% 的用户
内存消耗：23.8 MB, 在所有 Python3 提交中击败了5.13% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> idx list
        memo = defaultdict(list)
        for i, s in enumerate(strs):
            k = tuple(sorted(Counter(s).items()))
            memo[k].append(i)        
        return [[strs[idx] for idx in idx_list] for k, idx_list in memo.items()]

'''
执行用时：84 ms, 在所有 Python3 提交中击败了11.91% 的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了5.13% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> idx list
        memo = defaultdict(list)
        for i, s in enumerate(strs):
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            k = tuple(freq)
            memo[k].append(i)
        return [[strs[idx] for idx in idx_list] for k, idx_list in memo.items()]


'''
执行用时：64 ms, 在所有 Python3 提交中击败了32.69% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了16.47% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> str list
        memo = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            k = tuple(freq)
            memo[k].append(s)
        return list(memo.values())

'''
执行用时：52 ms, 在所有 Python3 提交中击败了72.58% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了62.88% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key -> str list
        memo = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            memo[k].append(s)
        return list(memo.values())








