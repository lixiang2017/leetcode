'''
prefix sum
T: O(N^2)
S: O(N)

执行用时：184 ms, 在所有 Python3 提交中击败了31.44% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了92.27% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        pre = [0] + list(accumulate(nums))
        ans = 0
        n = len(nums)
        for i in range(n - firstLen + 1):
            # i -> i + firstLen - 1
            f1 = pre[i + firstLen] - pre[i]
            if i >= secondLen:
                for j in range(i - secondLen + 1):
                    f2 = pre[j + secondLen] - pre[j]
                    ans = max(ans, f1 + f2)
            if i + firstLen + secondLen <= n:
                for j in range(i + firstLen, n - secondLen + 1):
                    f2 = pre[j + secondLen] - pre[j]
                    ans = max(ans, f1 + f2)                    
        return ans 


'''
prefix sum + heap
T: O(NlogN)
S: O(N)

执行用时：28 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了7.22% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if firstLen < secondLen:
            firstLen, secondLen = secondLen, firstLen
        pre = [0] + list(accumulate(nums))
        ans = 0
        n = len(nums)
        # for second, j -> j + secondLen - 1
        h = [(pre[j] - pre[j + secondLen], j, j + secondLen - 1) for j in range(firstLen, n - secondLen + 1)]
        heapify(h)
        for i in range(n - firstLen + 1):
            # i -> i + firstLen - 1
            f1 = pre[i + firstLen] - pre[i]
            if i >= secondLen:
                # i - secondLen -> i - 1
                f2 = pre[i] - pre[i - secondLen]
                heappush(h, (-f2, i - secondLen, i - 1))
            while h and (i <= h[0][2] <= i + firstLen - 1 or i <= h[0][1] <= i + firstLen - 1):
                heappop(h)
            if h:
                ans = max(ans, f1 - h[0][0])
        return ans 


'''
0x3f
prefix sum
T: O(N)
S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了82.99% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了34.54% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans 
            maxSumA = 0
            for i in range(firstLen + secondLen, len(s)):
                maxSumA = max(maxSumA, s[i - secondLen] - s[i - secondLen - firstLen])
                ans = max(ans, maxSumA + s[i] - s[i - secondLen])
        f(firstLen, secondLen)
        f(secondLen, firstLen)
        return ans 

'''
0x3f
prefix sum
T: O(N)
S: O(N)

执行用时：24 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.13% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = maxSumA = maxSumB = 0
        for i in range(firstLen + secondLen, len(s)):
            maxSumA = max(maxSumA, s[i - secondLen] - s[i - firstLen - secondLen])
            maxSumB = max(maxSumB, s[i - firstLen] - s[i - firstLen - secondLen])
            ans = max(ans, maxSumA + s[i] - s[i - secondLen], maxSumB + s[i] - s[i - firstLen])
        return ans 



