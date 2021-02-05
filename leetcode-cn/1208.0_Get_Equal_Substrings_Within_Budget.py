'''
approach: Sliding Window / Two Pointers
Time: O(N)
Space: O(N)

执行结果：通过
显示详情
执行用时：68 ms, 在所有 Python 提交中击败了44.44%的用户
内存消耗：23.1 MB, 在所有 Python 提交中击败了6.67%的用户
'''

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        costs = [abs(ord(chars) - ord(chart)) for chars, chart in zip(s, t)]
        size = len(s)
        i = j = currentCost = longest = 0
        while i < size and j < size + 1:
            if currentCost <= maxCost:
                longest = max(longest, j - i)
                if j < size:
                    currentCost += costs[j]
                j += 1
            else:
                currentCost -= costs[i]
                i += 1
        
        return longest    
