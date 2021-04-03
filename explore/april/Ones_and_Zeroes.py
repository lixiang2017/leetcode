'''
52 / 69 test cases passed.
Status: Wrong Answer
Submitted: 0 minutes ago
Input:
["1100","100000","011111"]
6
6
Output:
1
Expected:
2
'''


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [(oneStr.count('0'), oneStr.count('1')) for oneStr in strs]
        count.sort(key=lambda cnt: (cnt[0] * 1.0 / m + cnt[1] * 1.0 / n))
        
        for i, (zero, one) in enumerate(count):
            m -= zero
            n -= one
            if m < 0 or n < 0:
                return i
            
        return len(strs)
        


'''
You are here!
Your memory usage beats 31.03 % of python submissions.

ref:
https://leetcode-cn.com/problems/ones-and-zeroes/solution/pythonjian-dan-yi-dong-de-jie-fa-by-semi-9fu3/
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [(oneStr.count('0'), oneStr.count('1')) for oneStr in strs]
        # number of '0', number of '1', size of subset
        ans = {(0, 0, 0)}
        
        for zero, one in count:
            ans |= {(zero + z, one + o, c + 1) for z, o, c in ans if z + zero <= m and o + one <= n}
        return max(cnt for _, _, cnt in ans)
        

