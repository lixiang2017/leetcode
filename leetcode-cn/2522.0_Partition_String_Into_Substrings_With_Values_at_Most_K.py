'''
greedy, one pass

执行用时：104 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了0.00% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 1
        t = 0
        for ch in s:
            i = int(ch)
            if i > k:
                return -1
            t = t * 10 + i
            if t > k:
                ans += 1
                t = i 
        return ans 

'''
执行用时：116 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了0.00% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans, x = 1, 0
        for v in map(int, s):
            if v > k:
                return -1
            x = x * 10 + v 
            if x > k:
                ans += 1
                x = v
        return ans 

        