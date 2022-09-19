'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.05% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了79.57% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

'''
执行用时：44 ms, 在所有 Python3 提交中击败了60.26% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了62.82% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pairs = list(c.items())
        pairs.sort(key = lambda p: (p[1], -p[0]))
        ans = []
        for k, cnt in pairs:
            ans += [k] * cnt
        return ans 

'''
one line 
执行用时：44 ms, 在所有 Python3 提交中击败了60.26% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了44.23% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lru_cache(None)(lambda x: (nums.count(x), -x)))
