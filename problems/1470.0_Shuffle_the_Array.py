'''
Runtime: 58 ms, faster than 88.71% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.1 MB, less than 86.30% of Python3 online submissions for Shuffle the Array.
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pairs = [[nums[i], nums[i + n]] for i in range(n)]
        return list(chain(*pairs))

'''
Runtime: 65 ms, faster than 60.58% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.3 MB, less than 33.52% of Python3 online submissions for Shuffle the Array.
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] *(2 * n)
        for i in range(n):
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[n + i]
        return ans 
        