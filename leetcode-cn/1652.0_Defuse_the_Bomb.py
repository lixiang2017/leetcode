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
