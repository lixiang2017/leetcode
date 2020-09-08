#
# @lc app=leetcode id=896 lang=python
#
# [896] Monotonic Array
#
'''
Success
Details 
Runtime: 436 ms, faster than 87.60% of Python online submissions for Monotonic Array.
Memory Usage: 16.8 MB, less than 100.00% of Python online submissions for Monotonic Array.
'''
# @lc code=start
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        if 1 == l:
            return True

        is_increasing = False
        is_decreasing = False
        for i in range(1, l):
            if A[i] == A[i-1]:
                continue
            elif A[i] > A[i-1]:
                is_increasing = True
            else:
                is_decreasing = True

            if is_increasing and is_decreasing:
                return False    

        return True


        
if __name__ == '__main__':
    A = [1,2,2,3]
    assert Solution().isMonotonic(A) == True

    A =  [6,5,4,4]
    assert Solution().isMonotonic(A) == True

    A = [1,3,2]
    assert Solution().isMonotonic(A) == False

    A = [1,2,4,5]
    assert Solution().isMonotonic(A) == True
    
    A = [1,1,1]
    assert Solution().isMonotonic(A) == True

    A = [3] * 50000
    assert Solution().isMonotonic(A) == True

    A = [5]
    assert Solution().isMonotonic(A) == True


# @lc code=end

