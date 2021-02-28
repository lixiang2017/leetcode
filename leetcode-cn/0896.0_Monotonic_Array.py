'''
Time: O(N + N) = O(N)
Space: O(1)

执行用时：424 ms, 在所有 Python 提交中击败了84.31%的用户
内存消耗：18.1 MB, 在所有 Python 提交中击败了24.51%的用户
'''


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        return self.isIncreasing(A, N) or self.isDecreasing(A, N)
    
    def isIncreasing(self, A, N):
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                return False
        return True
    
    def isDecreasing(self, A, N):
        for i in range(N - 1):
            if A[i] < A[i + 1]:
                return False
        return True

'''

执行用时：552 ms, 在所有 Python 提交中击败了5.88%的用户
内存消耗：18 MB, 在所有 Python 提交中击败了45.10%的用户
'''

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        inc = des = True
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                inc = False
            if A[i] < A[i + 1]:
                des = False
        
        return inc or des


'''

执行用时：448 ms, 在所有 Python 提交中击败了36.27%的用户
内存消耗：17.5 MB, 在所有 Python 提交中击败了99.02%的用户
'''
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        inc = des = True
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                inc = False
            if A[i] < A[i + 1]:
                des = False
            
            if not inc and not des:
                return False
        
        return inc or des




'''
approach: Sort
Time: O(NlogN + NlogN + N + N) = O(NlogN)
Space: O(N + N) = O(N)

执行用时：444 ms, 在所有 Python 提交中击败了40.20%的用户
内存消耗：18.2 MB, 在所有 Python 提交中击败了17.65%的用户
'''

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A == sorted(A) or A == sorted(A, reverse=True)


'''

执行用时：428 ms, 在所有 Python 提交中击败了76.47%的用户
内存消耗：17.7 MB, 在所有 Python 提交中击败了85.29%的用户
'''


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        notMono = 0
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                notMono += 1
                break
                
        for i in range(N - 1):
            if A[i] < A[i + 1]:
                notMono += 1
                break
            
        if notMono == 2:
            return False
        
        return True
