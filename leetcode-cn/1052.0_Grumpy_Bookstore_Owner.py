'''
approach: Sliding Window / Two Pointers
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：332 ms, 在所有 Python 提交中击败了11.76%的用户
内存消耗：15 MB, 在所有 Python 提交中击败了37.25%的用户
'''

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        current = sum(customers[:X]) + \
            sum(customers[i] for i in range(X, len(customers)) if not grumpy[i])
        maximum = current
        for left in range(0, len(customers) - X):
            if grumpy[left]:
                current -= customers[left]
            right = left + X
            if grumpy[right]:
                current += customers[right]
            maximum = max(current, maximum)

        return maximum
