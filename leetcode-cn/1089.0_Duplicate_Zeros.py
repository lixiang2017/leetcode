'''
T: O(2N), S:O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了92.14% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了23.87% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i, new_arr = 0, []
        while len(new_arr) < n:
            if arr[i] != 0:
                new_arr.append(arr[i])
            else:
                new_arr.append(0)
                if len(new_arr) < n:
                    new_arr.append(0)
                else:
                    break
            i += 1
        arr[:] = new_arr[:]

