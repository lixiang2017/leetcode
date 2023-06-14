'''
sort, bisect.insort

执行用时：680 ms, 在所有 Python3 提交中击败了6.82% 的用户
内存消耗：22.1 MB, 在所有 Python3 提交中击败了13.64% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        bits = []
        for i, f in enumerate(flips, 1):
            insort(bits, f)
            ans += i == bits[-1]
        return ans 

'''
sum 

执行用时：84 ms, 在所有 Python3 提交中击败了79.55% 的用户
内存消耗：21.4 MB, 在所有 Python3 提交中击败了27.27% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = total = should = 0
        for i, f in enumerate(flips, 1):
            total += f
            should += i 
            ans += total == should 
        return ans 
