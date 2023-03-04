'''
hash table

执行用时：3284 ms, 在所有 Python3 提交中击败了37.25% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了74.51% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter(x & y for x in nums for y in nums)
        return sum(c for x in nums for mask, c in cnt.items() if x & mask == 0)

'''
二进制枚举子集
sub = (sub - 1) & x 

执行用时：648 ms, 在所有 Python3 提交中击败了76.47% 的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了47.06% 的用户
'''
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter(x & y for x in nums for y in nums)        
        ans = 0
        for x in nums:
            sub = x = x ^ 0xFFFF
            while True:
                ans += cnt[sub]
                if sub == 0:
                    break
                sub = (sub - 1) & x 

        return ans 
