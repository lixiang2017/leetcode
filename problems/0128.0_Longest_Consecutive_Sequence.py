'''
meet in the middle -> away from the middle
看完了题目，就想着排序。 然后，我就去洗澡了，然后我就想到了这个方法。
T： O（2 * N）
S： O（N）

Runtime: 615 ms, faster than 52.11% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 28.5 MB, less than 42.76% of Python3 online submissions for Longest Consecutive Sequence.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        while seen:
            i = seen.pop()
            l, r = i - 1, i + 1
            while l in seen:
                seen.remove(l)
                l -= 1
            while r in seen:
                seen.remove(r)
                r += 1
            ans = max(ans, r - l - 1)
        
        return ans 
