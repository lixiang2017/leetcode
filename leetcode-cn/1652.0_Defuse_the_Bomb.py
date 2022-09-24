'''
approach: Iteration + Two Pointers / Sliding Window
Time: O(N)
Space: O(N)

执行用时：28 ms, 在所有 Python 提交中击败了56.41%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了48.37%的用户
'''


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(code)
        decode = [0] * size
        if k == 0: return [0] * size

        preSum = 0
        if k > 0:
            preSum = sum(code[0 : k])
        else:
            preSum = sum(code[k - 1 : -1])
        
        for i in range(size):
            if k > 0:
                preSum += code[(i + k) % size]
            else:
                preSum += code[(i - 1) % size]
            if k > 0:
                preSum -= code[(i) % size]
            else:
                preSum -= code[(i + k - 1) % size]
            decode[i] = preSum
        
        return decode


'''
simulation, brute force
T: O(NK)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了30.35% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.49% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        for i in range(n):
            t = 0
            k0 = k
            while k0 != 0:
                t += code[(i + k0) % n]
                if k0 > 0:
                    k0 -= 1
                else:
                    k0 += 1
            ans[i] = t
        return ans 


'''
滚动更新前缀和 =》 滑动窗口
T: O(N)
S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了78.60% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了12.84% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        # first one
        t = 0
        k0 = k
        while k0 != 0:
            t += code[k0 % n]
            if k0 > 0:
                k0 -= 1
            else:
                k0 += 1
        # iteration for every one 
        for i in range(n):
            ans[i] = t
            if k > 0:
                t -= code[(i + 1) % n]
                t += code[(i + k + 1) % n]
            else:
                t += code[i % n]
                t -= code[(i + k) % n]
        return ans

