'''
two pointers, meet in the middle
T: O(N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了85.42% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了88.89% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        i, j = 1, n 
        ans = []
        while k > 0:
            ans.append(i)
            i += 1
            k -= 1
            if k <= 0:
                break 
            ans.append(j)
            j -= 1
            k -= 1
        # i...j
        if ans[-1] == i - 1:
            ans.extend(range(i, j + 1))
        else:
            ans.extend(range(j, i - 1, -1))
        return ans 


'''
meet in the middle
T: O(N)
S: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了40.25% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了77.36% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        left, right = 1, n 
        while k > 2:
            ans.append(left)
            ans.append(right)
            left += 1
            right -= 1
            k -= 2

        if 2 == k:
            ans.append(left)
            left += 1
            ans.extend(range(right, left - 1, -1))
        else:
            ans.extend(range(left, right + 1))
        return ans 


'''
执行用时：48 ms, 在所有 Python3 提交中击败了25.79% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了67.92% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n - k))
        i, j = n - k, n 
        while i <= j:
            ans.append(i)
            if i != j:
                ans.append(j)
            i, j = i + 1, j - 1
        return ans 
        