'''
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
        # print 'sumAB: ', sumAB

        for i in range(size - 1):
            for j in range(i + 1, size):
                if target - (nums[i] + nums[j]) in sumAB:
                    for p, q in sumAB[target - (nums[i] + nums[j])]:
                        if len(set([i, j, p, q])) == 4 and sorted([nums[p], nums[q], nums[i], nums[j]]) not in quadruplets:
                            # print 'sorted: ', sorted([i, j, p, q])
                            quadruplets.append(sorted([nums[p], nums[q], nums[i], nums[j]]))
        
        return quadruplets
