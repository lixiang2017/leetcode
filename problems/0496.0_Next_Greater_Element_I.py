'''
Stack / Monotonic Stack
降序的stack
T: O(M + N)
S: O(N)

Runtime: 65 ms, faster than 45.85% of Python3 online submissions for Next Greater Element I.
Memory Usage: 14.7 MB, less than 14.67% of Python3 online submissions for Next Greater Element I.
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, greater = [], dict()
        for x in nums2:
            while stack and stack[-1] < x:
                greater[stack.pop()] = x
            stack.append(x)
        return [greater.get(x, -1) for x in nums1]


'''
T: O(MN)

Runtime: 76 ms, faster than 33.04% of Python3 online submissions for Next Greater Element I.
Memory Usage: 14.6 MB, less than 14.67% of Python3 online submissions for Next Greater Element I.
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [next((y for y in nums2[nums2.index(x): ] if y > x), -1) for x in nums1]
