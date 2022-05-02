'''
Runtime: 102 ms, faster than 53.59% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.7 MB, less than 17.91% of Python3 online submissions for Sort Array By Parity.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2]


'''
sort

Runtime: 84 ms, faster than 81.12% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x % 2 != 0)
        return nums


'''
sort

Runtime: 91 ms, faster than 67.73% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: 1 if x % 2 != 0 else 0)
        return nums

'''
sort 

Runtime: 139 ms, faster than 20.62% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.7 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: 12342 if x % 2 != 0 else 324)
        return nums

'''
sort

Runtime: 79 ms, faster than 90.70% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.7 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: 32 if x % 2 != 0 else -40)
        return nums


