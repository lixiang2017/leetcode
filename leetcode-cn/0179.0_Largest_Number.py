'''
wrong answer

'''

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        # wrong compare
        def compare(s):
            # '6' -> '6' * 10
            # '66' -> '6' * 10
            # '6666' -> '6' * 10
            if 1 == len(set(s)):
                return s[0] * 10
            else:
                return s

        # wrong compare too
        def compare1(s):
            # '1113' -> '1113333333...'
            # '111311' -> '11131111111...'
            N = len(s)
            return s + (10 - N) * s[-1]

        nums.sort(key = compare1, reverse = True)
        return ''.join(nums)

'''
[10,2]
[3,30,34,5,9]
[666, 6663, 6668]
[1113, 111311]
'''

'''
执行结果：
解答错误
显示详情
输入：
[34323,3432]
输出：
"343233432"
预期结果：
"343234323"
'''


'''
approach: Sort

执行用时：32 ms, 在所有 Python 提交中击败了49.57%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了59.60%的用户
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        def compare(a, b):
            if a + b > b + a:
                return 1
            else:
                return -1

        nums.sort(key = cmp_to_key(compare), reverse = True)
        return ''.join(nums) if nums[0][0] != '0' else '0'


'''
执行用时：36 ms, 在所有 Python 提交中击败了40.11%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了27.51%的用户
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        
        nums = sorted(map(str, nums), \
            key=cmp_to_key(lambda a, b: (a + b > b + a) - (a + b < b + a)), \
            reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'




