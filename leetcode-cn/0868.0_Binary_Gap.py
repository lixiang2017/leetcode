'''
执行用时：40 ms, 在所有 Python3 提交中击败了42.18% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了76.53% 的用户
通过测试用例：261 / 261
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        zero_cnt = None
        while n:
            if n & 1:
                if zero_cnt is not None:
                    ans = max(ans, zero_cnt + 1)
                zero_cnt = 0
            else:
                if zero_cnt is not None:
                    zero_cnt += 1
            n >>= 1
        return ans 

'''
执行用时：44 ms, 在所有 Python3 提交中击败了14.29% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.71% 的用户
通过测试用例：261 / 261
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        zero_cnt = -1
        while n:
            if n & 1:
                if zero_cnt != -1:
                    ans = max(ans, zero_cnt + 1)
                zero_cnt = 0
            else:
                if zero_cnt != -1:
                    zero_cnt += 1
            n >>= 1
        return ans 

'''
执行用时：40 ms, 在所有 Python3 提交中击败了42.18% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了67.35% 的用户
通过测试用例：261 / 261
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        zero_cnt = -99
        while n:
            if n & 1:
                ans = max(ans, zero_cnt)
                zero_cnt = 1
            else:
                zero_cnt += 1
            n >>= 1
        return ans 


'''
执行用时：32 ms, 在所有 Python3 提交中击败了92.52% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了57.48% 的用户
通过测试用例：261 / 261
'''
idx_map = {1 << i: i for i in range(30)}

class Solution:
    def binaryGap(self, n: int) -> int:
        def lowbit(x: int) -> int:
            return x & (-x)
        
        last, ans = inf, 0
        while n:
            n -= (cur := lowbit(n))
            ans, last = max(ans, idx_map[cur] - last), idx_map[cur]
        return ans 

   

        