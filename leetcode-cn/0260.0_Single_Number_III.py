'''
bit manipulation
T: O(2N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了42.59% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了52.32% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        shift = len(bin(xor)) - 3
        a = b = 0
        for x in nums:
            if (x >> shift) & 1:
                a ^= x
            else:
                b ^= x
        return a, b


'''
hash table, T: O(N), S:O(N)

执行用时：32 ms, 在所有 Python3 提交中击败了86.81% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了11.68% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return list(filter(lambda x: c[x] == 1, nums))
