'''
do not forget to use abs
T: O(N)
S: O(1)

执行用时：88 ms, 在所有 Python3 提交中击败了74.25% 的用户
内存消耗：21.5 MB, 在所有 Python3 提交中击败了25.33% 的用户
通过测试用例：28 / 28
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            a = abs(x)
            nums[a - 1] *= -1
            if nums[a - 1] > 0:
                ans.append(a)
        return ans 

'''
原地hash / swap
T: O(N)
S: O(1)

执行用时：116 ms, 在所有 Python3 提交中击败了21.52% 的用户
内存消耗：21.4 MB, 在所有 Python3 提交中击败了35.74% 的用户
通过测试用例：28 / 28
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [x for i, x in enumerate(nums) if i != x - 1]



'''
原地hash / swap
T: O(N)
S: O(1)

执行用时：108 ms, 在所有 Python3 提交中击败了30.79% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了96.19% 的用户
通过测试用例：28 / 28
'''
'''
[4,3,2,7,8,2,3,1]

swap for indices:  0 3 swap num  4 7
after swap:  [7, 3, 2, 4, 8, 2, 3, 1]
swap for indices:  0 6 swap num  7 3
after swap:  [3, 3, 2, 4, 8, 2, 7, 1]
swap for indices:  0 2 swap num  3 2
after swap:  [2, 3, 3, 4, 8, 2, 7, 1]
swap for indices:  0 1 swap num  2 3
after swap:  [3, 2, 3, 4, 8, 2, 7, 1]
-- index  0 done.
-- index  1 done.
-- index  2 done.
-- index  3 done.
swap for indices:  4 7 swap num  8 1
after swap:  [3, 2, 3, 4, 1, 2, 7, 8]
swap for indices:  4 0 swap num  1 3
after swap:  [1, 2, 3, 4, 3, 2, 7, 8]
-- index  4 done.
-- index  5 done.
-- index  6 done.
-- index  7 done.
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                # print('swap for indices: ', i, nums[i] - 1, "swap num ", nums[i], nums[nums[i] - 1])
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # https://stackoverflow.com/questions/68152730/understand-python-swapping-why-is-a-b-b-a-not-always-equivalent-to-b-a-a
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]  # wrong
                # print('after swap: ', nums)
            # print('-- index ', i, 'done.')
        return [x for i, x in enumerate(nums) if i != x - 1]


