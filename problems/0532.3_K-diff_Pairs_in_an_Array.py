'''
hash table + sort

Runtime: 169 ms, faster than 14.18% of Python3 online submissions for K-diff Pairs in an Array.
Memory Usage: 15.8 MB, less than 40.07% of Python3 online submissions for K-diff Pairs in an Array.
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            c = Counter(nums)
            ans = 0
            for x, cnt in c.items():
                if cnt > 1:
                    ans += 1
            return ans
        else:
            ans = 0
            s_nums = set(nums)
            u_nums = list(s_nums)
            u_nums.sort()
            for x in u_nums:
                if x + k in s_nums:
                    ans += 1
            return ans
    
