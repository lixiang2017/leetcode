'''
prefix sum

执行用时：620 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：29 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        sub = set()
        n = len(nums)
        div = [0] * n
        for i, x in enumerate(nums):
            if x % p == 0:
                div[i] = 1
                
        pre = [0] + list(accumulate(div))
        for i in range(n):
            for j in range(i, n):
                if pre[j + 1] - pre[i] <= k:
                    sub.add(tuple(nums[i: j + 1]))
        
        return len(sub)


'''
直接count

执行用时：680 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：28.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        sub = set()
        n = len(nums)

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                sub.add(tuple(nums[i: j + 1]))
        
        return len(sub)

