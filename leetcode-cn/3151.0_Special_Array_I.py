class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((x + y) % 2 for x, y in pairwise(nums))

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((x + y) % 2 == 1 for x, y in pairwise(nums))

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return not any((x + y) % 2 == 0 for x, y in pairwise(nums))