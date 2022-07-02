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
