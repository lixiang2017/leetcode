'''
                if j > 0 and subarr[j] == subarr[j - 1]: ##!!!!
                    continue

执行用时：52 ms, 在所有 Python3 提交中击败了94.22% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了76.94% 的用户
通过测试用例：162 / 162
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        q, r = divmod(s, k)
        if r != 0 or max(nums) > q:
            return False 
        
        nums.sort(reverse=True)
        n = len(nums)
        self.ans = False 

        def dfs(i, subarr):
            if self.ans:
                return
            if i == n:
                if subarr == [q] * k:
                    self.ans = True
                return 
            
            for j in range(k):
                if j > 0 and subarr[j] == subarr[j - 1]: ##!!!!
                    continue
                if subarr[j] + nums[i] <= q:
                    dfs(i + 1, subarr[: j] + [subarr[j] + nums[i]] +  subarr[j + 1: ])
            
        dfs(0, [0] * k)
        return self.ans

'''
[4,3,2,3,5,2,1]
4
[1,2,3,4]
3
[3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2]
10
[3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
5
[10,1,10,9,6,1,9,5,9,10,7,8,5,2,10,8]
11
'''


'''
backtracking

执行用时：56 ms, 在所有 Python3 提交中击败了88.27% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了78.17% 的用户
通过测试用例：162 / 162
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        q, r = divmod(s, k)
        if r != 0 or max(nums) > q:
            return False 
        
        nums.sort(reverse=True)
        n = len(nums)
        self.ans = False 
        bucket = [0] * k

        def dfs(i):
            if self.ans:
                return
            if i == n:
                if bucket == [q] * k:
                    self.ans = True
                return 
            
            for j in range(k):
                if j > 0 and bucket[j] == bucket[j - 1]: ##!!!!
                    continue
                if bucket[j] + nums[i] <= q:
                    bucket[j] += nums[i]
                    dfs(i + 1)
                    bucket[j] -= nums[i]
            
        dfs(0)
        return self.ans
