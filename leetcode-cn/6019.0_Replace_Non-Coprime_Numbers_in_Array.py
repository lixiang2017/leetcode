'''
stack

执行用时：224 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：71 / 71
'''

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = [1]
        for x in nums:
            while True:
                g = gcd(ans[-1], x)
                if g == 1:
                    ans.append(x)
                    break
                else:
                    x *= ans.pop() // g

        return ans[1: ]

