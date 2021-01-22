'''


执行结果：通过
显示详情
执行用时：268 ms, 在所有 Python 提交中击败了75.81%的用户
内存消耗：
13.7 MB, 在所有 Python 提交中击败了34.15%的用户
'''


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        total = []
        carry = 0
        while A or K:
            # low digit from A and K
            if A:
                lowA = A.pop()
            else:
                lowA = 0
            if K:
                lowK = K % 10
                K /= 10
            else:
                lowK = 0
            carry, lowDigit = divmod(lowA + lowK + carry, 10)
            total.append(lowDigit)
        
        if carry:
            total.append(carry)

        return total[:: -1]
        
