'''
Counter + Sort

Runtime: 568 ms, faster than 19.16% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
Memory Usage: 30.1 MB, less than 52.25% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        for x in sorted(c.keys()):
            if c[x] == 0:
                continue
            for j in range(1, k):
                if x + j not in c or c[x] > c[x + j]:
                    return False
                c[x + j] -= c[x]
        return True

'''
Counter + Sort

Runtime: 640 ms, faster than 14.09% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
Memory Usage: 30.1 MB, less than 52.25% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        c = Counter(nums)
        for x in sorted(c.keys()):
            if c[x] == 0:
                continue
            for j in range(1, k):
                if x + j not in c or c[x] > c[x + j]:
                    return False
                c[x + j] -= c[x]
        return True
