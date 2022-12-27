'''
sort

Runtime: 922 ms, faster than 97.37% of Python3 online submissions for Maximum Bags With Full Capacity of Rocks.
Memory Usage: 22.3 MB, less than 49.34% of Python3 online submissions for Maximum Bags With Full Capacity of Rocks.
'''
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = [c - r for c, r in zip(capacity, rocks)]
        need.sort()
        full = 0
        for x in need:
            if x > additionalRocks:
                break
            else:
                full += 1
                additionalRocks -= x
        return full
