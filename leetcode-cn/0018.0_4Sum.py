'''
这个代码现在会超时了，20220430
287 / 289 个通过测试用例
状态：超出时间限制

[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
200



Time: O(N ^ 2 * log(M)), M is the length of quadruplets
Space: O(N ^ 2)

执行结果：通过
显示详情
执行用时：
120 ms, 在所有 Python 提交中击败了71.84%的用户
内存消耗：
18.3 MB, 在所有 Python 提交中击败了5.34%的用户
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        quadruplets = []
        sumAB = defaultdict(list)
        size = len(nums)
        for i in range(size - 1):
            for j in range(i + 1, size):
                sumAB[nums[i] + nums[j]].append([i, j])

        for i in range(size - 1):
            for j in range(i + 1, size):
                if target - (nums[i] + nums[j]) in sumAB:
                    for p, q in sumAB[target - (nums[i] + nums[j])]:
                        if len(set([i, j, p, q])) == 4 and sorted([nums[p], nums[q], nums[i], nums[j]]) not in quadruplets:
                            quadruplets.append(sorted([nums[p], nums[q], nums[i], nums[j]]))
        
        return quadruplets


'''
# preprocess, 同样的数字多余四个没有用，最多保留四个


执行用时：268 ms, 在所有 Python3 提交中击败了73.56% 的用户
内存消耗：21.9 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：289 / 289
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # preprocess
        c = Counter(nums)
        for k in c:
            if c[k] > 4:
                c[k] = 4
        nums = list(c.elements())

        # two sum -> position pair list
        twosum2pos = defaultdict(list)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                twosum2pos[s].append([i, j])

        ans_set = set()
        for i in range(n - 1):
            for j in range(n):
                s = target - nums[i] - nums[j]
                for p, q in twosum2pos[s]:
                    if len(set([i, j, p, q])) == 4:
                        a = tuple(sorted(nums[p] for p in [i, j, p, q]))
                        ans_set.add(a)

        ans = [list(a) for a in ans_set]
        return ans 
  


'''
排序去重， for + for + two pointers
T: O(N^3)
S: O(1)

执行用时：88 ms, 在所有 Python3 提交中击败了82.47% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.33% 的用户
通过测试用例：289 / 289
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break 
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue 
                p, q = j + 1, n - 1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1
                    elif s > target:
                        q -= 1
                    else:
                        p += 1

                    while p < q and p > j + 1 and nums[p] == nums[p - 1]:
                        p += 1
                    while p < q and q < n - 1 and nums[q] == nums[q + 1]:
                        q -= 1

        return ans


