'''
apporach: 2D-DP -> DP with Space Compression
Time: O(steps * min(steps, arrLen))
Space :O(min(steps, arrLen))

key points:
no need to allocate O(arrLen) space, just need O(min(steps, arrLen)),
because you cannot reach out of steps length within steps.
由于一共执行 steps 步操作，因此指针所在下标一定不会超过 steps，可以将 j 的取值范围进一步缩小到 
0 ≤ j ≤ min(arrLen−1,steps)。

ref:
https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/ting-zai-yuan-di-de-fang-an-shu-by-leetcode-soluti/

执行用时：300 ms, 在所有 Python3 提交中击败了67.07%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了94.61%的用户
'''



class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        # N = arrLen  # TLE
        if arrLen <= 1:
            return 1
        N = min(steps + 1, arrLen)

        pre = [1, 1] + [0] * (N - 2)
        after = [0] * N
        for _ in range(steps - 1):
            for i in range(N):
                if 0 == i:
                    after[i] = (pre[i] + pre[i + 1]) % MOD
                elif N - 1 == i:
                    after[i] = (pre[i - 1] + pre[i]) % MOD
                else:
                    after[i] = (pre[i - 1] + pre[i] + pre[i + 1]) % MOD
                # after[i] %= MOD  # need!!!
            # pre, after = after, pre  # right
            pre = after[:]  # right
            # pre = after   # wrong

        return pre[0]



'''
输入：
27
7
输出：
71127785002
预期结果：
127784505
'''

