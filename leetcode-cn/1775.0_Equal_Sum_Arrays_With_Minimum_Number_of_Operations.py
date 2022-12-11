'''
hash table + greedy
T: O(M + N)
S: O(1)

执行用时：104 ms, 在所有 Python3 提交中击败了86.09% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了20.00% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if 6 * m < n or 6 * n < m:
            return -1
        c1, c2 = Counter(nums1), Counter(nums2)
        total1, total2 = sum(x * c for x, c in c1.items()), sum(x * c for x, c in c2.items())
        if total1 < total2:
            total1, total2 = total2, total1 
            c1, c2 = c2, c1 
        for i in range(1, 7):
            c1[i] += c2[7 - i]
        diff = total1 - total2
        ans = 0
        for i in range(6, 1, -1):
            if c1[i] * (i - 1) >= diff:
                ans += (diff + i - 2) // (i - 1)
                break
            else:
                ans += c1[i]
                diff -= c1[i] * (i - 1)
        return  ans 
