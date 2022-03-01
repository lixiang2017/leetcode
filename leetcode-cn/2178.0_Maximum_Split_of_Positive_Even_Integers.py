'''
binary search

执行用时：88 ms, 在所有 Python3 提交中击败了88.49% 的用户
内存消耗：24.4 MB, 在所有 Python3 提交中击败了86.19% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        '''
        2    4   6  8 10 12 ...
        2*1 2*2 2*3 ... 2*k
        (1 + k) * k / 2 * 2 = (1 + k) * k
        '''
        if finalSum % 2:
            return []
        lo, hi = 0, int(sqrt(finalSum))
        k = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if (mid + 1) * mid <= finalSum:
                k = mid 
                lo = mid + 1
            else:
                hi = mid - 1
        
        ans = [2 * i  for i in range(1, k + 1)]
        ans[-1] += finalSum - (1 + k) * k
        return ans 


'''
lo, hi = 0, finalSum

执行用时：64 ms, 在所有 Python3 提交中击败了96.16% 的用户
内存消耗：24.2 MB, 在所有 Python3 提交中击败了99.62% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        '''
        2    4   6  8 10 12 ...
        2*1 2*2 2*3 ... 2*k
        (1 + k) * k / 2 * 2 = (1 + k) * k
        '''
        if finalSum % 2:
            return []
        # lo, hi = 0, int(sqrt(finalSum))
        lo, hi = 0, finalSum
        k = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if (mid + 1) * mid <= finalSum:
                k = mid 
                lo = mid + 1
            else:
                hi = mid - 1
        
        ans = [2 * i  for i in range(1, k + 1)]
        ans[-1] += finalSum - (1 + k) * k
        return ans 


'''
执行用时：76 ms, 在所有 Python3 提交中击败了92.84% 的用户
内存消耗：24.4 MB, 在所有 Python3 提交中击败了77.88% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        '''
        2    4   6  8 10 12 ...
        2*1 2*2 2*3 ... 2*k
        (1 + k) * k / 2 * 2 = (1 + k) * k
        '''
        if finalSum % 2:
            return []

        k = int(sqrt(finalSum))     
        ans = [2 * i  for i in range(1, k + 1)]
        ans[-1] += finalSum - (1 + k) * k
        if len(ans) >= 2 and ans[-1] <= ans[-2]:
            last = ans.pop()
            ans[-1] += last
        return ans 


        