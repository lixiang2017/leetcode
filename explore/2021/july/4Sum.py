'''
Brute Force
Time: O(N^4)
Space: O(1)

270 / 283 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        ans = set()
        for i in range(N - 3):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N - 1):
                    for l in range(k + 1, N):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
        return ans
        #return [list(a) for a in ans]
        
'''
Input: [-5,5,4,-3,0,0,4,-2]
4
Output: [[5,-3,4,-2],[-5,5,4,0],[-5,5,0,4],[5,4,-3,-2]]
Expected: [[-5,0,4,5],[-3,-2,4,5]]
'''

'''
224 / 283 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        twosum = defaultdict(list)
        for i in range(N - 1):
            for j in range(i + 1, N):
                twosum[nums[i] + nums[j]].append([nums[i], nums[j], i, j])
        
        ans = set()
        for s1, v1 in twosum.items():
            for s2, v2 in twosum.items():
                for l1 in v1:
                    for l2 in v2:
                        na, nb, i, j = l1
                        nc, nd, k, l = l2
                        if s1 + s2 == target and not (i == k or j == l or i == l or j == k):
                            ans.add(tuple(sorted([na, nb, nc, nd])))
        
        return ans
                

'''
282 / 283 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        twosum = defaultdict(list)
        for i in range(N - 1):
            for j in range(i + 1, N):
                twosum[nums[i] + nums[j]].append([nums[i], nums[j], i, j])
        
        ans = set()
        for s1, v1 in twosum.items():
            for s2, v2 in twosum.items():
                if s1 + s2 == target:
                    for l1 in v1:
                        for l2 in v2:
                            na, nb, i, j = l1
                            nc, nd, k, l = l2
                            if not (i == k or j == l or i == l or j == k):
                                ans.add(tuple(sorted([na, nb, nc, nd])))
        
        return ans
                


'''
Sort + Two Pointers
Time: O(NlogN + N^3) = O(N^3)
Space: O(logN) for sort

You are here!
Your runtime beats 28.47 % of python3 submissions.
You are here!
Your memory usage beats 78.23 % of python3 submissions.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        i = j = k = l = 0
        ans = []
        while i < N - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < N - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                k, l = j + 1, N - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
                    elif s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                j += 1
            i += 1
        return ans

'''
Input: [-2,-1,-1,1,1,2,2]
0
Output: [[-2,-1,1,2],[-2,-1,1,2],[-1,-1,1,1]]
Expected: [[-2,-1,1,2],[-1,-1,1,1]]    
'''



'''
Sort + Two Pointers
Time: O(NlogN + N^3) = O(N^3)
Space: O(logN) for sort

You are here!
Your runtime beats 92.94 % of python3 submissions.
You are here!
Your memory usage beats 28.76 % of python3 submissions.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        i = j = k = l = 0
        ans = []
        while i < N - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[N - 1] + nums[N - 2] + nums[N - 3] < target:
                i += 1
                continue
            j = i + 1
            while j < N - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[N - 1] + nums[N - 2] < target:
                    j += 1
                    continue
                k, l = j + 1, N - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
                    elif s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                j += 1
            i += 1
        return ans


'''
Sort + Two Pointers
Time: O(NlogN + N^3) = O(N^3)
Space: O(logN) for sort

You are here!
Your runtime beats 95.49 % of python3 submissions.
You are here!
Your memory usage beats 92.86 % of python3 submissions.
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        nums.sort()
        N = len(nums)
        for i in range(N - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[N - 1] + nums[N - 2] + nums[N - 3] < target:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            for j in range(i + 1, N - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[N - 1] + nums[N - 2] < target:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                    
                k, l = j + 1, N - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                        # k += 1  # wrong answer
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                        # l -= 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
                    elif total > target:
                        l -= 1
                    else:
                        k += 1
        
        return quadruplets
        
