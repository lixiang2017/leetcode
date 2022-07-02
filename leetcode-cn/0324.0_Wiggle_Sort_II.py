'''
一刀切开成两半。双指针分别从中间和末尾，逆序添加。
sort + two pointers
T: O(NlogN + N)
S: O(logN + N)

执行用时：40 ms, 在所有 Python3 提交中击败了96.69% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了78.61% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, arr = len(nums), sorted(nums)
        i, j = (n - 1) // 2, n - 1
        idx = 0
        while j > (n - 1) // 2:
            nums[idx] = arr[i]
            i -= 1
            idx += 1
            nums[idx] = arr[j]
            j -= 1
            idx += 1
        if i == 0:
            nums[n - 1] = arr[0]
