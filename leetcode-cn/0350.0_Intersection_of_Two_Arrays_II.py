'''
hash table

执行用时：28 ms, 在所有 Python3 提交中击败了97.54% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.46% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        ans= []
        if len(cnt1) > len(cnt2):
            cnt1, cnt2 = cnt2, cnt1
        for x, c in cnt1.items():
            c2 = cnt2[x]
            ans.extend([x] * min(c, c2))
        return ans 

'''
执行用时：36 ms, 在所有 Python3 提交中击败了76.76% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.46% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
        