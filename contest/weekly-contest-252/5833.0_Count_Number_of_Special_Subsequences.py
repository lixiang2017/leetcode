'''
ref:
https://leetcode-cn.com/circle/discuss/pAXboA/

99 / 99 个通过测试用例
状态：通过
执行用时: 1668 ms
内存消耗: 18.9 MB
提交时间：9 小时前
'''
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        pre_0 = pre_1 = pre_2 = 0
        post_0 = post_1 = post_2 = 0
        N = len(nums)
        for i in range(N):
            if 0 == nums[i]:  # `+=` !!!, not `=`
                post_0 += pre_0 + 1
            elif 1 == nums[i]:
                post_1 += pre_0 + pre_1
            elif 2 == nums[i]:
                post_2 += pre_1 + pre_2
            pre_0, pre_1, pre_2 = post_0, post_1, post_2
        
        return post_2 % MOD
                

'''
DP

执行用时：1628 ms, 在所有 Python3 提交中击败了33.33% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了33.33% 的用户
'''
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        zero = one = two = 0
        for i in range(len(nums)):
            if 0 == nums[i]:
                # 三种情况
                # 1、以当前0为结尾；（之前的zero串接上这个0）
                # 2、不以当前0为结尾（以上一个0为结尾）；（使用之前的zero串，不用当前0）
                # 3、以当前0为开始;（不使用之前的，仅使用当前的这个0）
                zero = zero + zero + 1
            elif 1 == nums[i]:
                # 三种情况
                # 1、之前的zero串，接上这个1；
                # 2、单独之前的one串；不使用这个1
                # 3、之前的one串，接上这个1；
                one = zero + one + one
            else:
                # 三种情况
                # 1、之前的one串，接上这个2
                # 2、单独之前的two串；不使用这个2
                # 3、之前的two串，接上这个2              
                two = one + two + two

        return two % MOD

