'''
T: O(3N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了76.12% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了94.03% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        j = i + 1
        while j < n and arr[j] < arr[i]:
            j += 1
        j -= 1
        while j > 0 and arr[j - 1] == arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr 


'''
执行用时：44 ms, 在所有 Python3 提交中击败了46.27% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了8.96% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                j = len(arr) - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr 
        