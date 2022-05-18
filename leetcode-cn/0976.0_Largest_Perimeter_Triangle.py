'''
sort, T: O(NlogN + N^3), S: O(1)

执行用时：104 ms, 在所有 Python3 提交中击败了6.27% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了92.62% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        largest = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[j] * 2 <= nums[i]:
                    break
                if nums[j] * 2 + nums[i] <= largest:
                    break 
                for k in range(j + 1, n):
                    if nums[j] + nums[k] <= nums[i]:
                        break
                    if nums[i] + nums[j] + nums[k] <= largest:
                        break 
                    if nums[j] + nums[k] > nums[i]:
                        largest = max(largest, nums[i] + nums[j] + nums[k])         

        return largest


'''
为什么排序遍历相邻元素可行，有没有可能最优解为非相邻元素？（不会）

证明：反证 假设 a , b, c 为最优解，且存在a',b',满足 a < a' < b < b' < c（存在非相邻元素）

    由于 a + b > c，a < a', 有 a' + b > c，(a', b, c)优于(a, b, c),与(a, b, c)为最优解矛盾，故不存在a'
    b'同理不存在 由于 a + b > c, b < b'，有a + b' > c，(a, b, c)为最优解矛盾，故不存在b'

因此最优解一定为排序后相邻元素
'''

'''
sort, T: O(NlogN + N), S: O(1)

执行用时：52 ms, 在所有 Python3 提交中击败了82.91% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了29.69% 的用户
通过测试用例：84 / 84
'''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        for i in range(n - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0



'''
sort, T: O(NlogN + N), S: O(1)

执行用时：68 ms, 在所有 Python3 提交中击败了18.68% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了60.23% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0
