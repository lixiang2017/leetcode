'''
288 / 288 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.1 MB
提交时间：12 小时前
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return [k for k, v in Counter(chain(set(nums1), set(nums2), set(nums3))).items() if v > 1]
        

'''
执行用时：40 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：288 / 288
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list(s1&s2 | s2&s3 | s1&s3)


'''
执行用时：40 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：288 / 288
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = [0] * 101
        for x in nums1:
            mask[x] |= 1
        for x in nums2:
            mask[x] |= 2
        for x in nums3:
            mask[x] |= 4
        ans = []
        for i, m in enumerate(mask):
            if m > 2 and m != 4:
                ans.append(i)
        return ans

'''
执行用时：32 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：288 / 288
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        s = s1 | s2 | s3
        ans = []
        for x in s:
            f1 = 1 if x in s1 else 0
            f2 = 1 if x in s2 else 0
            f3 = 1 if x in s3 else 0
            if f1 + f2 + f3 >= 2:
                ans.append(x)
        return ans
        