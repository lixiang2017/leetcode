'''
hash table + sort 

执行用时：64 ms, 在所有 Python3 提交中击败了25.26% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了87.37% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        if 0 == k:
            for x, c in cnt.items():
                # ans += c * (c + 1) // 2
                if c > 1:
                    ans += 1
        else:
            nums = sorted(cnt.keys())
            n = len(nums)
            j = 0
            for i, x in enumerate(nums):
                while j < n and nums[j] - x < k:
                    j += 1
                if j < n and nums[j] - x == k:
                    # ans += cnt[x] * cnt[nums[j]]
                    ans += 1
        return ans 
    

'''
nums = sorted(cnt)

执行用时：52 ms, 在所有 Python3 提交中击败了43.60% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了84.88% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        if 0 == k:
            for x, c in cnt.items():
                # ans += c * (c + 1) // 2
                if c > 1:
                    ans += 1
        else:
            nums = sorted(cnt)
            n = len(nums)
            j = 0
            for i, x in enumerate(nums):
                while j < n and nums[j] - x < k:
                    j += 1
                if j < n and nums[j] - x == k:
                    # ans += cnt[x] * cnt[nums[j]]
                    ans += 1
        return ans 
    


