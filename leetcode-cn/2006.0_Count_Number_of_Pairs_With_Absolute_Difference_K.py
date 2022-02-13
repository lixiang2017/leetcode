'''
brute force
T: O(N^2)
S: O(1)

执行用时：268 ms, 在所有 Python3 提交中击败了5.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.63% 的用户
通过测试用例：237 / 237
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans 

'''
hash table
T: O(N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了92.71% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.83% 的用户
通过测试用例：237 / 237
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # num to indice list
        indice = [[] for _ in range(101)]
        for i, x in enumerate(nums):
            indice[x].append(i)
        ans = 0
        for i in range(1, 101):
            if i + k > 100:
                break
            # if indice[i] and indice[i + k]:
            # 1, 4, 7, 9      2, 5, 6, 10
            ans += len(indice[i]) * len(indice[i + k])
        return ans 
